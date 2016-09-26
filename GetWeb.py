from bs4 import BeautifulSoup as BS
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def GetPageHtml(url):
	req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept':'text/html;q=0.9,*/*;q=0.8',
	'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding':'gzip',
	'Connection':'close',
	'Referer': None 
	}
	req_timeout = 5
	req = urllib2.Request(url, None, req_header)
	resp = urllib2.urlopen(req, None, req_timeout)
	html = resp.read()
	return html.decode('gbk')




def GetWebDic():
	pagedict = {}
	path = "http://www.ce.cn"
	f = GetPageHtml(path)
	soup = BS(f, 'html.parser')

	targetlist = soup.find_all(has_class)
	target = targetlist[0]
	y = target.find_all(has_href)
	count = 0
	for href in y:
		name = ""
		#print href.prettify()
		if href.b:
			name = href.b
		else:
			name = href.string
		pagedict[name] = href["href"]

	return pagedict

def DealWithContent(url):
	contentlist = []
	html = GetPageHtml(url)
	soup = BS(html, 'html.parser')
	targetlist = soup.find_all(has_neirong)
	target = targetlist[0]
	for y in target:
		if y.name == "p":
			if y.span:
				contentlist.append(str(y))
	return contentlist



def has_class(tag):
	if tag.has_attr('class'):
		for x in tag['class']:
			if x == "hotnews":
				return 1
		return 0
	else:
		return 0

def has_href(tag):
	return tag.has_attr("href")

def has_neirong(tag):
	if tag.has_attr('class'):
		for x in tag['class']:
			if x == 'Custom_UnionStyle':
				return 1
		return 0
	else:
		return 0

#def has_empty_style(tag):
