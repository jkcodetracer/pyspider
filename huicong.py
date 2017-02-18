#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class QSBK:
	def __init__(self):		
		self.pageIndex = 1

		#url = 'http://www.qiushibaike.com/hot/'
		#url = 'http://www.qiushibaike.com/hot/page/1/?s=4936167'
		self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
		self.headers = {'User-Agent' : self.user_agent}
		self.stories = []
		self.enable = False
	
	def getPage(self, pageIndex):
		try: 
			url = 'http://www.qiushibaike.com/hot/page/'+ str(pageIndex)+'/?s=4936167'
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError, e:
			if hasattr(e, "code"):
				print e.code
			if hasattr(e, "reason"):
				print e.reason

	def getPageItems(self, pageIndex):
			#pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?'+ \
			#		        'content"><span>(.*?)</span>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
			content = self.getPage(pageIndex)
			if not content:
				print "load failed!"
				return None

			pattern = re.compile('<h2>(.*?)</h2>',re.S)
			name_items = re.findall(pattern, content)
		
			pattern = re.compile('content">.*?<span>(.*?)</span>', re.S)
			content_items = re.findall(pattern, content)
		
			pattern = re.compile('<i class="number">(.*?)</i>', re.S)
			laugh_number = re.findall(pattern, content)
		
			pageStories = []
			for i in range(len(name_items)):
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR, "\n", content_items[i])
				pageStories.append([name_items[i].strip(),
					content_items[i].strip(),
					laugh_number[i].strip()])

			return pageStories

	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1
	
	def getOneStory(self, pageStories, page):
		for story in pageStories:
			input = raw_input()
			self.loadPage()
			if input == 'Q':
				self.enable = False
				return
			print u"page(%d)\t user:(%s)\tgood(%s)\n%s" %(page,story[0],story[1],story[2])

	# user interface!
	def start(self):
		print u"load pages, (N)next (Q)exit"
		self.enable = True
		self.loadPage()
		nowPage = 0
		
		while self.enable:
			if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()


