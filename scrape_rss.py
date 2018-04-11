#!/usr/bin/env python3
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import json
import sys

urls_tmp = []

urls = {
    "atom": [],
    "rss": []
}


def get_content_type(url):
    try:
        f = urllib.request.urlopen(url)
        content_header = (f.info().get("Content-Type"))
        if ";" in content_header:
            content_splitted = content_header.split(";")
            content_type = content_splitted[0]
        else:
            content_type = content_header
    except:
        content_type = "NETWORK ERROR"
    return content_type


d = pq(sys.stdin.read(), parser='html')

for a in d('a,link'):
    tmp = a.attrib['href']
    if (re.search('^https?://.*', tmp)):
        urls_tmp.append(tmp)

for link in urls_tmp:
    ct = get_content_type(link)
    print ("ct url", ct, link)
    if ct == "application/rss+xml":
        urls["rss"].append(link)
    elif ct == "application/atom+xml":
        urls["atom"].append(link)

print (json.dumps(urls, indent=4))
