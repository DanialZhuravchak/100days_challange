"""Download a website."""
import mechanize


def viewPage(url):
    """View webpage and download html code."""
    browser = mechanize.Browser()
    page = browser.open(url)
    source_code = page.read()
    print(source_code)


viewPage('http://www.syngress.com/')
