#!/usr/bin/env python3
"""Collect the hiring email addresses a company publishes on its own site.

Reads a CSV of companies (column `company`, optional `website`, `slug`), visits the
company's careers/jobs/contact pages, and writes the generic hiring addresses found
there (careers@, jobs@, recruiting@, talent@, hr@ ...) with the page each came from.

Rules, on purpose:
  * Only addresses that appear verbatim on the page (plain text, mailto: links, or
    Cloudflare's obfuscated form). Addresses are never guessed or constructed.
  * Only the company's own domain, and only hiring-style local parts. Personal
    addresses of named employees are ignored.
  * robots.txt is honored for every URL via tools/robots_check.py (cautious rules:
    an unreadable robots.txt means no fetch).
  * One request at a time per company, with a delay between requests.

Usage:
  python3 tools/careers_emails.py --companies job_scraper/nish/visa_companies.csv \
      --out job_scraper/nish/hr_contacts.csv [--limit 50] [--delay 2]
"""

import argparse, csv, functools, html, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import robots_check

# robots.txt is read once per host, not once per page
robots_check._fetch = functools.lru_cache(maxsize=None)(robots_check._fetch)

UA = 'Mozilla/5.0 (compatible; careers-email-lookup; personal job search)'
PATHS = ['/careers', '/jobs', '/careers/', '/join-us', '/work-with-us', '/contact', '/about']
LINK_HINT = re.compile(r'career|jobs|join|work-with-us|hiring|opportunit', re.I)
HIRING = re.compile(
    r'^(careers?|jobs?|recruit(ing|ment|ers?)?|talent|hr|humanresources|people|'
    r'hiring|join|work|apply|applications?|staffing|ta)([._+-].*)?$', re.I)
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
CF = re.compile(r'/cdn-cgi/l/email-protection#([0-9a-fA-F]+)')


def decode_cf(hexstr):
    b = bytes.fromhex(hexstr)
    return ''.join(chr(c ^ b[0]) for c in b[1:])


def extract_emails(page, site_host):
    """Hiring-style addresses on the company's own domain, verbatim from `page`."""
    text = html.unescape(page)
    found = set(EMAIL.findall(text))
    found.update(decode_cf(h) for h in CF.findall(text) if len(h) > 2 and len(h) % 2 == 0)
    base = site_host.lower().removeprefix('www.')
    out = set()
    for e in found:
        local, _, dom = e.lower().rpartition('@')
        if (dom == base or dom.endswith('.' + base) or base.endswith('.' + dom)) and HIRING.match(local):
            out.add(e.lower())
    return sorted(out)


def get(url, delay):
    rc, why = robots_check.gate(url)
    if rc != 0:
        return None, why
    time.sleep(delay)
    r = subprocess.run(['curl', '-sSL', '--max-time', '25', '--max-redirs', '4', '-A', UA,
                        '-w', '\n%{http_code}', '--', url],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    body, _, code = r.stdout.rpartition('\n')
    return (body, 'ok') if code == '200' else (None, 'HTTP ' + code)


def candidate_sites(row):
    if row.get('website'):
        yield row['website'] if '://' in row['website'] else 'https://' + row['website']
        return
    slug = re.sub(r'[^a-z0-9]', '', (row.get('slug') or row['company']).lower())
    for tld in ('com', 'io', 'ai', 'co', 'dev', 'app'):
        yield f'https://www.{slug}.{tld}'


def name_matches(row, page):
    title = re.search(r'<title[^>]*>(.*?)</title>', page, re.I | re.S)
    tokens = [t for t in re.split(r'\W+', row['company'].lower()) if len(t) > 2]
    return bool(title and tokens and tokens[0] in html.unescape(title.group(1)).lower())


def run(row, delay):
    for site in candidate_sites(row):
        home, _ = get(site, delay)
        if home is None or (not row.get('website') and not name_matches(row, home)):
            continue
        host = urlsplit(site).netloc
        urls = [urljoin(site, p) for p in PATHS]
        for href in re.findall(r'href=["\']([^"\']+)["\']', home)[:400]:
            u = urljoin(site, href)
            if urlsplit(u).netloc.endswith(host.removeprefix('www.')) and LINK_HINT.search(urlsplit(u).path):
                urls.append(u.split('#')[0])
        seen, hits = set(), []
        for u in [site] + urls:
            if u in seen or len(seen) >= 8:
                continue
            seen.add(u)
            body, _ = (home, 'ok') if u == site else get(u, delay)
            for e in extract_emails(body or '', host):
                hits.append((e, u))
        return host, hits
    return None, []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--companies', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--delay', type=float, default=2.0)
    ap.add_argument('--workers', type=int, default=8, help='companies fetched in parallel (one request at a time per company)')
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.companies, encoding='utf-8')))
    rows = rows[:a.limit] if a.limit else rows
    with open(a.out, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['company', 'site', 'email', 'found_on'])
        with ThreadPoolExecutor(a.workers) as ex:
            for i, (row, (host, hits)) in enumerate(zip(rows, ex.map(lambda r: run(r, a.delay), rows)), 1):
                for e, u in dict.fromkeys(hits):
                    w.writerow([row['company'], host, e, u])
                f.flush()
                print(f"[{i}/{len(rows)}] {row['company']}: {host or 'site not found'}, {len(set(hits))} address(es)")

if __name__ == '__main__':
    main()
