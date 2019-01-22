from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    new_url = 'https://mars.nasa.gov/news/'
    browser.visit(new_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    print(f"Title: {news_title}")
    print(f"Para: {news_paragraph}")

    return listings