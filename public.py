# encoding=utf-8
import urllib
import urllib2
import re

class Tool:
    #去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')

    def replace(self,x):
        #strip()将前后多余内容删除
        return x

def load_page(url):
	user_agent = 'Mzilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebK/537.36(KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
	headers = {'User-Agent':user_agent}
	if not url:
		return ""

	try:
		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request, timeout = 5)
		content = response.read().decode('gbk')
		return content

	except urllib2.URLError, e:
		print e.reason
		return ""
	except Exception, e:
		print url
		return ""

def fetch_info(htm, content, encode = False):
	pattern = re.compile(htm, re.S)
	lis = re.findall(pattern, content)
	if encode and lis:
		lis[0].encode('utf-8')

	if not lis:
		lis.append(" ")

	return lis


