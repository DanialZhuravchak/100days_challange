"""Change UserAgent."""
import mechanize


def testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = userAgent
    page = browser.open(url)
    source_code = page.read()
    print(source_code)


url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
userAgent = [('User-agent', 'Mozilla/5.0 (X11; U; ' +
              'Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')]
testUserAgent(url, userAgent)
