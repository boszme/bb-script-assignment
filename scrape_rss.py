#!/usr/bin/env python3
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re
import json

urlok = {
    "atom": [],
    "rss": []
}


d = pq("<html><head><link href=\"http://link.html\">link</link></head><body><a href=\"egy.html\">egy</a><a href=\"http://ketto.html\">ketto</a><a href=\"https://harom.html\">harom</a></body></html>")
#d = pq(etree.fromstring("<html></html>"))

for a in d('a,link'):
    tmp = a.attrib['href']
    if (re.search('https?://.*', tmp)):
        urlok["atom"].append(tmp)

print (json.dumps(urlok, indent=4))
