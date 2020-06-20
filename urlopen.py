#!/usr/bin/env python


import urllib2
from urllib2 import Request, urlopen, URLError

def getresp(url):
    print(url)
    response = urllib2.urlopen(url)
    print("URL: %s\n", response.url)
    print("Code: ", response.code)
    #return response

getresp("http://www.google.com")

