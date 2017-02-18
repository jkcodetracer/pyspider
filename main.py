#!/usr/bin/python
from public import fetch_info,load_page, Tool
import pymongo
import time
import re
import multiprocessing

def get_main_list(url):
	content = load_page(url)
	if not content:
		print "fetch main page failed!"
		return []

	main_list = fetch_info('<a rel="nofollow" href="(.*?)" target=.*?</a>', \
			content)
	#print main_list
	return main_list

def add_url_tail(url):
	rptail = re.compile('com\Z')
	new_url = re.sub(rptail, "com/shop/company.html", url)
	return new_url

def fetch_from_item(url):
	personal = {}
	content = load_page(url)

	tool = Tool()

	if not content:
		return []
	#telnum
	htm = 'telIco">.*?<b>(.*?)</b>'
	personal["telnum"] = tool.replace(fetch_info(htm, content))
	# phone
	htm = 'telIco2">.*?cInfoRig">(.*?)</div>'
	personal["phone"] = tool.replace(fetch_info(htm, content))
	# user
	htm = 'userIco">.*?cInfoRig">.*?<em>(.*?)</div>'
	personal["user"] = tool.replace(fetch_info(htm, content, True))
	#company
	htm = 'cNameIco ">.*?cInfoRig">(.*?)</div>'
	personal["company"] = tool.replace(fetch_info(htm, content, True))

	
	return personal

def fetch_from_shop(url):
	personal = {}
	content = load_page(url)

	tool = Tool()

	if not content:
		return []
	#telnum
	htm = '"tel01 floatleft">(.*?)</li>'
	personal["telnum"] = tool.replace(fetch_info(htm, content, True))
	#phone
	htm = 'li class="tel02 floatleft">(.*?)</li>'
	personal["phone"] = tool.replace(fetch_info(htm, content, True))
	#user
	htm = '<span class="bluezzbold font14".*?>(.*?)</span>'
	personal["user"] = tool.replace(fetch_info(htm, content, True))
	#company
	htm = '"blackbold font14" >(.*?)</span>'
	personal["company"] = tool.replace(fetch_info(htm, content, True))


	return personal


def iter_pages(myurl, db):
	for i in range(1,101):
		if i == 1:
			cturl = myurl
		else:
			cturl = myurl + '&ee='+str(i) + '&ap=B'
		content = load_page(cturl)
		print "make url: ",cturl 
		if not content:
			continue

		htm = '<a data-detailbcid=.*?href="(.*?)".*?>'
		inner_list = fetch_info(htm, content)
		inner_list = list(set(inner_list))
		if i % 20:
			time.sleep(5)


		for url in inner_list:
			info_list = []
			new_url = add_url_tail(url)
			print new_url
			if new_url == url:
				info_list = fetch_from_item(new_url)
			else:
				info_list = fetch_from_shop(new_url)
			
			if not info_list:
				continue
			db['infor'].insert(info_list)


'''
db = pymongo.MongoClient('localhost', 27017)['Phone']

# for test
url = 'http://www.hc360.com/'
get_main_list(url)
url = 'http://yechangfu.b2b.hc360.com/shop/company.html'
text1 = fetch_from_shop(url)
url =  "http://b2b.hc360.com/supplyself/523448619.html" 
text2 = fetch_from_item(url)

db = pymongo.MongoClient('localhost', 27017)['Phone']
db['infor'].insert(text1)
db['infor'].insert(text2)
'''
def process(num):
	print "!!!!!!", num
	for i in range(avg):
		pos = i+num
		print num, "current url: ", main_list[pos]
		iter_pages(main_list[pos], db)


url = 'http://www.hc360.com/'
db = pymongo.MongoClient('localhost', 27017)['Phone']
main_list = get_main_list(url)
total = len(main_list)
avg = total/4
print total
for i in range(4):
	p = multiprocessing.Process(target = process, args = (i*avg,))
	p.start()
'''
for url in main_list:
	print "current url: ", url
	time.sleep(3)
	iter_pages(url, db)
'''


