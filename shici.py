#!/usr/bin/env python
#coding: utf-8

import requests
import re
"""
功能： 随机产生一首古诗
"""

r = requests.get("http://www.shicimingju.com//chaxun/shicirand/?i=90")

r.encoding = "utf-8"
title_and_author_r = re.compile(r"<a href=\"(.*?)\">(.*?)<\/a>")
content_r = re.compile(r"<div class=\"(.*?)\">(.*?)<\/div>")
try:
    title = title_and_author_r.findall(r.text)[0][1]
    author = title_and_author_r.findall(r.text)[1][1]
    content = content_r.findall(r.text)[1][1].replace("<br>","\n")
    print title
    print author
    print content
except Exception as e:
    print "error" 
