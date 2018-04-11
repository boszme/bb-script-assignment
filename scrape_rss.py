#!/usr/bin/env python3
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import json
import sys

urls = {
    "atom": [],
    "rss": []
}


def get_content_type(url):
    f = urllib.request.urlopen(url)
    content_header = (f.info().get("Content-Type"))
    if ";" in content_header:
        content_type, charset = content_header.split(";")
    else:
        content_type = content_header
    return content_type


d = pq(sys.stdin.read(), parser='html')

for a in d('a,link'):
    tmp = a.attrib['href']
    if (re.search('https?://.*', tmp)):
        urls["atom"].append(tmp)



print (json.dumps(urls, indent=4))
