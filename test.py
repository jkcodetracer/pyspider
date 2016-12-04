#!/usr/bin/python

import urllib2
enable_proxy = True
proxy_headler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
print null_proxy_handler

request = urllib2.Request('http://www.xxxxx.com')
try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	print e.reason

