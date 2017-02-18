#!/usr/bin/python

import urllib
import urllib2
import re
import multiprocessing


# main page
user_agent =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebK/537.36(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
headers = {'User-Agent': user_agent}
url = 'http://www.hc360.com/'

request = urllib2.Request(url, headers = headers)

try:
	mfile = open("test.txt", "w+")

	response = urllib2.urlopen(request)
	content = response.read()
	pattern = re.compile('<a rel="nofollow" href="(.*?)" target=.*?</a>')
	main_list = re.findall(pattern, content)

	for url in main_list:
		mfile.write(url)
		mfile.write('\n')
except urllib2.URLError, e:
	print e.reason


page = 1
#url = 'http://s.hc360.com/?w=%B9%E0%D7%B0%BB%FA&mc=seller&ee='+ str(page) + '&ap=B'
url = 'http://s.hc360.com/?w=%B9%E0%D7%B0%BB%FA&mc=seller'

request = urllib2.Request(url, headers = headers)

try:
	response = urllib2.urlopen(request)
	#content = response.read().decode('utf-8')
	content = response.read()
	pattern  = re.compile('<a data-detailbcid=.*?href="(.*?)".*?>')
	inner_list = re.findall(pattern, content)

	rptail = re.compile('com\Z')
	inner_list = list(set(inner_list))
	new_list = [re.sub(rptail, "com/shop/company.html", url) for url in inner_list ]
	for url in new_list:
		print url
except urllib2.URLError, e:
	print e.reason


url = "http://b2b.hc360.com/supplyself/523448619.html"
httpHandler = urllib2.HTTPHandler(debuglevel = 1)
httpsHandler = urllib2.HTTPSHandler(debuglevel = 1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
request = urllib2.Request(url, headers = headers)
try: 
	response = urllib2.urlopen(request)
	#content = response.read()
	content = response.read().decode('gbk')
	#print content
	pattern = re.compile('telIco">.*?<b>(.*?)</b>', re.S)
	telnum = re.findall(pattern, content)

	pattern = re.compile('telIco2">.*?cInfoRig">(.*?)</div>')
	phone = re.findall(pattern, content)

	pattern = re.compile('userIco">.*?cInfoRig">.*?<em>(.*?)</div>', re.S)
	user = re.findall(pattern, content)

	pattern = re.compile('cNameIco ">.*?cInfoRig">(.*?)</div>')
	company = re.findall(pattern, content)

	print telnum
	print phone
	print user[0].encode('utf-8')
	print company[0].encode('utf-8')

except urllib2.URLError, e:
	print e.reason


url = 'http://yechangfu.b2b.hc360.com/shop/company.html'
request = urllib2.Request(url, headers = headers)
try:
	response = urllib2.urlopen(request)
	content = response.read().decode('gbk')
	pattern = re.compile('"tel01 floatleft">(.*?)</li>')
	telnum = re.findall(pattern, content)

	pattern = re.compile('li class="tel02 floatleft">(.*?)</li>')
	phone = re.findall(pattern, content)

	pattern = re.compile('<span class="bluezzbold font14".*?>(.*?)</span>')
	user = re.findall(pattern, content)

	pattern = re.compile('"blackbold font14" >(.*?)</span>')
	company = re.findall(pattern, content)
	print telnum[0].encode('utf-8')
	print phone[0].encode('utf-8')
	print user[0].encode('utf-8')
	print company[0].encode('utf-8')

except urllib2.URLError, e:
	print e.reason

print multiprocessing.cpu_count()

for i in range(4):
	print i*5

