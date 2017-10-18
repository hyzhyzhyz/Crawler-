#encoding:utf-8
import time
from lxml import html
import requests
from urllib2 import urlopen
import urllib
import numpy

nums=[1]
nums.extend(range(25,250,25))
file=[]
for num in nums:
    file.append('https://www.douban.com/doulist/212485/?start='+str(num)+'&sort=seq&sub_type=')
movie_name=[]
movie_star=[]
for url in file:
    print url
    page = requests.get(url, headers=None)
    #print page.text
    tree = html.fromstring(page.text)
    movie_name_xpath='//div[@class="bd doulist-subject"]/div[@class="title"]/a/text()'
    movie_star_xpath='//div[@class="bd doulist-subject"]/div[@class="abstract"]/text()'
    news = tree.xpath(movie_name_xpath)
    
    for cont in news:
        movie_name.append(cont.encode('utf-8'))
    news = tree.xpath(movie_star_xpath)
    for cont in news:
        if "主演" in cont.encode('utf-8'):
            movie_star.append(cont.encode('utf-8') ) 
    #time.sleep(5)
sum_movie=0
for name, star in zip(movie_name,movie_star) :
    if  "布拉德·皮特" in star:
        sum_movie+=1
        print name
print sum_movie 

