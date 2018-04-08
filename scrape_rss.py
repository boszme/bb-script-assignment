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

d = pq(sys.stdin.read(), parser='html')

for a in d('a,link'):
    tmp = a.attrib['href']
    if (re.search('https?://.*', tmp)):
        urls["atom"].append(tmp)

print (json.dumps(urls, indent=4))
