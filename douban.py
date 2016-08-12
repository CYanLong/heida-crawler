#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
import json
from scrapy.selector import Selector
import logging
logging.basicConfig(level=logging.DEBUG)
def getDataById(mid):
	'''根据电影id得到电影的详细描述信息:title, desc picUrl

	'''
	itemUrl = 'https://api.douban.com/v2/movie/' + mid
	
	itemJson = requests.get(itemUrl)
	
	itemData = json.loads(itemJson.content.decode('utf-8'))
	#得到json数据,解析并拼接返回结果.
	rate = itemData['rating']['average'] #评分
	numRaters = itemData['rating']['numRaters'] #评论人数
	#描述
	desc =  '\n\n原名: ' + itemData['title'] + '\n\n豆瓣评分: ' + str(itemData['rating']['average']) + '(' + str(itemData['rating']['numRaters']) +  '人评)' + '\n\n 剧情简介: ' + itemData['summary'] + '\n\n 豆瓣链接:' + itemUrl
	title = itemData['alt_title']
	picUrl = itemData['image']
	return title, desc, picUrl

def getMovieBySub(tag="经典"):
	
	req_param = {
		"type": "movie",
		"tag": tag,
		"sort": "rank",
		"page_limit": 20,
		"page_start": 0
	}
	
	sub_url = 'https://movie.douban.com/j/search_subjects'

	resp = requests.get(sub_url, params = req_param)
	
	li = json.loads(resp.content.decode('utf-8'))['subjects']
	print(str(li).encode('utf-8'))
	item = li[0]
	#print(str(item).encode('utf-8'))
	itemUrl = item['url']
	#电影的id
	mid = itemUrl.split('/')[-2]
	
	return getDataById(mid)

def getMovieByName(movieName):
	'''根据电影名得到电影详细信息,首先得到mid,调用getDataById得到详细信息
	'''
	search_url = 'https://movie.douban.com/subject_search?search_text=' + movieName
	
	resp = requests.get(search_url)

	items = Selector(text=resp.content.decode('utf-8')).xpath('//div[@class="article"]/div/table[@width="100%"]/tr[@class="item"]/td[@valign="top"]/a/@href').extract()
	logging.debug(items)
	if len(items) == 0:
		return "无法找到"
	
	else:
		#只取第一项
		mid = items[0].split('/')[-2]
		logging.debug(mid)
		return getDataById(mid)

#测试
if __name__ == '__main__':
	#getMovieBySub("纪录片")

	#getMovieByName('Sprin')
