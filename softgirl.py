import urllib
import re
import time

def getHtml2(url2):
    html2=urllib.urlopen(url2).read().decode('utf-8')
    return html2

def gettopic(html2):
    reg2=r'http://www.douban.com/group/topic/\d+'
    topiclist=re.findall(reg2,html2)
    x=0
    for topicurl in topiclist:
        x+=1
    return topicurl

def download(topic_page):
    reg3=r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg'
    imglist=re.findall(reg3,topic_page)
    i=1
    download_img=None
    for imgurl in imglist:
        print imgurl
        img_numlist=re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            str = 'D:/temp/%s.jpg'%img_num
            print "will download"
            print str
            download_img=urllib.urlretrieve(imgurl,str)
            time.sleep(1)
            i+=1
            print(imgurl)
    return download_img

page_end=int(input('input end page number:'))
num_end=page_end*25
num=0
page_num=1
while num<=num_end:
    html2=getHtml2('http://www.douban.com/group/kaopulove/discussion?start=%d'%num)
    topicurl=gettopic(html2)
    topic_page=getHtml2(topicurl)
    download_img=download(topic_page)
    num=page_num*25
    page_num+=1
else:
    print('OK')

