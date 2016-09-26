import GetWeb
import re

def cleantxt(label):
	pattern = re.compile(r'<.*?>')
	match = pattern.match(label)
	if match:
		print match.group()

path = r"f:\content.txt"
ff = open(path, 'a+')
targetdic = GetWeb.GetWebDic()
list1 = []
for v in targetdic.values():
	list1.append(v) 
labeldic =  GetWeb.DealWithContent(list1[0])
for label in labeldic:
	txt = label +"\r\n"
	cleantxt(label)
ff.close()

