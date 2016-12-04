#!/usr/bin/python

import urllib2
import cookielib

# cookie
cookie = cookielib.CookieJar()
# create cookie processor
handler = urllib2.HTTPCookieProcessor(cookie)
# create opener
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
	print 'Name = ', item.name
	print 'Value = ', item.value


