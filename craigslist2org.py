#!/usr/bin/env python
"""Generate org-mode entry from craigslist url

Usage:
  craigslist2org.py <url>
"""
import requests
from bs4 import BeautifulSoup
from docopt import docopt


def parse_craiglist(html_doc):
    soup = BeautifulSoup(html_doc, "lxml")

    price = soup.find_all(class_='postingtitletext')[0]\
                .find_all(class_='price')[0].string

    date = soup.find_all(id='display-date')[0]\
               .find_all('time')[0]['datetime']
    title = soup.find_all(id='titletextonly')[0].string

    return dict(title=title, price=price, posted_date=date)


def grab(url):
    html_doc = requests.get(url).text
    data = parse_craiglist(html_doc)
    data['url'] = url

    return prepare_org(data)


def prepare_org(data, header_level=1):
    return f"""
{'*'*header_level} [[{data.get('url','')}][{data['title']} - {data['price']}]]
:PROPERTIES:
:URL: {data.get('url', '')}
:PRICE: {data['price']}
:END:
"""


def test_parse_craigslist():
    filename = "6260272864.html"
    webdata = open(filename).read()
    data = parse_craiglist(webdata)

    assert data['title'] == "tv table/bookcase/entertainment console"
    assert data['price'] == "$20"
    assert data['posted_date'] == "2017-08-11T15:46:28-0700"


def test_prepare_org():
    filename = "6260272864.html"
    webdata = open(filename).read()
    data = parse_craiglist(webdata)

    print(prepare_org(data))


def main():
    args = docopt(__doc__)
    print(grab(args['<url>']))


if __name__ == '__main__':
    main()
