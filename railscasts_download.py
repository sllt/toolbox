#!/usr/bin/env python
#coding: utf-8

'''
download railscasts.com
args: your rss
'''
import requests
import xml.etree.ElementTree as ET
import  sys


def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_filename

def get_urls(rss):
    urls = []
    root  = ET.fromstring(rss)
    for i in root.iter():
        if i.tag == 'enclosure':
            urls.append(i.attrib['url'])
    return urls

def get_video():
    if len(sys.argv) != 2:
        print "usage: railscasts_download.py rss_url"
    else:
        r = requests.get(sys.argv[1])
        urls  = get_urls(r.text)
        for url in urls:
            print "-- start download ", url.split('/')[-1], " --"
            download_file(url)

if __name__ == "__main__":
    get_video()
