"""Scrape the pussy."""

from anonBrowser import *
ab = anonBrowser(proxies=[],
                 user_agents=[('User-agent', 'superSecretBroswer')])
for attempt in range(1, 5):
    ab.anonymize()
    print('[*] Fetching page')
    response = ab.open('http://kittenwar.com', timeout=5)
    for cookie in ab.cookie_jar:
        print(cookie)
