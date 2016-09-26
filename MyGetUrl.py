from bs4 import BeautifulSoup as BS
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def GetHtml(url):
	response = urllib2.urlopen("http://www.ce.cn")
	page =  response.read()
	page = page.decode('gbk')
	return page

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

def GetLink(tag):
	tagsoup = BS(tag,'html.parser')
	return tagsoup.find_all(has_href)

def showx(x):
	print x


path = r'f:\tt.txt'
f = open(path, 'r')
f = f.read()
soup = BS(f, 'html.parser')

targetlist = soup.find_all(has_class)
target = targetlist[0]
y = target.find_all(has_href)
count = 0
for href in y:
	print href.prettify()
	print href.string
	print count
	count += 1

print len(y)
#targetsoup = BS(target, 'html.parser')
#[showx(x) for x in targetlist]

