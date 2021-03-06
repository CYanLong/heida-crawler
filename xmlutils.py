#!/usr/bin/python
#-*- encoding=utf-8 -*-

'''
	author: cyanlong
	data: 2016-08-13
'''

import time

from lxml import etree
import logging

def respMessage(req_xml, content_str):
	'''回复普通消息
	'''	
	resp_xml = etree.Element('xml')
    
	toUserName = etree.SubElement(resp_xml, "ToUserName")
	
	toUserName.text = etree.CDATA(req_xml.find('FromUserName').text)
	
	fromUserName = etree.SubElement(resp_xml, "FromUserName")
	
	fromUserName.text = etree.CDATA(req_xml.find('ToUserName').text)
	
	createTime = etree.SubElement(resp_xml, 'CreateTime')
	
	createTime.text = str(int(time.time()))
	
	msgType = etree.SubElement(resp_xml, 'MsgType')
	
	msgType.text = etree.CDATA('text')
	
	content = etree.SubElement(resp_xml, 'Content')
	#logging.info("======content charset: %s ======" % chardet.detect(content_str)['encoding'])
	content.text = etree.CDATA(content_str)
	
	return resp_xml


def respImageAndText(req_xml, title, desc, picUrl):
	'''回复图文消息
	'''
	resp_xml = etree.Element('xml')
	toUserName = etree.SubElement(resp_xml, 'ToUserName')
	toUserName.text = etree.CDATA(req_xml.find('FromUserName').text)

	fromUserName = etree.SubElement(resp_xml, 'FromUserName')
	fromUserName.text = etree.CDATA(req_xml.find('ToUserName').text)

	createTime = etree.SubElement(resp_xml, 'CreateTime')
	createTime.text = etree.CDATA(str(int(time.time())))
	
	etree.SubElement(resp_xml, 'MsgType').text = etree.CDATA('news')

	etree.SubElement(resp_xml, 'ArticleCount').text = '1'

	articles = etree.SubElement(resp_xml, 'Articles')
	item = etree.SubElement(articles, 'item')
	etree.SubElement(item, 'Title').text = title
	etree.SubElement(item, 'Description').text = desc
	etree.SubElement(item, 'PicUrl').text = picUrl
	
	return resp_xml

def respMedia(req_xml):
	'''回复媒体信息,图片,音频等
	'''
	resp_xml = etree.Element('xml')
	toUserName = etree.SubElement(resp_xml, "ToUserName")
	toUserName.text = etree.CDATA(req_xml.find('FromUserName').text)
	fromUserName = etree.SubElement(resp_xml,"FromUserName")
	fromUserName.text = etree.CDATA(req_xml.find('ToUserName').text)

	createTime = etree.SubElement(resp_xml, "CreateTime")
	createTime.text = str(int(time.time()))

	msgType = etree.SubElement(resp_xml, 'MsgType')
	msgType.text = etree.CDATA(req_xml.find('MsgType').text)
	
	image = etree.SubElement(resp_xml, 'Image')
	mediaId = etree.SubElement(image, 'MediaId')
	mediaId.text = etree.CDATA(req_xml.find('MediaId').text)

	return resp_xml
