#!/usr/bin/python
#coding=utf-8
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
import urllib
import os
import time

def get_page_from(channel,pages):  
    if pages==1:
    	channel=channel+'/page'  
    else:
  	channel=channel+'/page/{}'.format(pages)  
    web_data=requests.get(channel) 
    soup=BeautifulSoup(web_data.text,'lxml')  
    if soup.find('body > div.main > div.main-content > div.currentpath'):
        pass  
    else:  
        lists = soup.select('ul#pins > li > span > a')  
        for list in lists: 
	    #print(list.get('href')[list.get('href').rindex('/')+1:]) 
	    path=list.get('href')[list.get('href').rindex('/')+1:]
            #path='{}'.format(list.get_text().encode('utf-8'))  
            isExists = os.path.exists(path)  
            if not isExists:  
                print("[*]mkdir " + path + "...")  
                os.mkdir(path)  
            else:  
                print("[+]mk " + path + 'sucess')  
            for i in range(1,101):  
                get_list_info(list.get('href'),i,path)
		time.sleep(1)  

def get_list_info(url,page,mmpath):  
    web_data=requests.get(url)  
    soup=BeautifulSoup(web_data.text,'lxml')  
    src=soup.select('body > div.main > div.content > div.main-image > p > a > img')  
    for srcc in src:  
        image_url=srcc.get('src').split('net')[1].split('01.')[0]
    	if page < 10:  
        	pages='0'+str(page)  
    	else:  
        	pages =str(page)  
   	url_split='http://i.meizitu.net'+image_url+'{}.jpg'.format(pages)  
	try:  
        	name = url_split.split('/')[5].split('.')[0]  
		data = urlopen(url_split).read()  
	        fileName = '{}/meizi'.format(mmpath) + name + '.jpg'  
        	fph = open(fileName, "wb")  
	        fph.write(data)  
        	fph.flush()  
	        fph.close()  
        except Exception:  
    		 print('[!]Address Error!!!!!!!!!!!!!!!!!!!!!')  

def get_mei_channel(url):
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    channel=soup.select('body > div.main > div.main-content > div.postlist > dl.tags > dd > a')
    for list in channel:
        callback.append(list.get('href'))
    return callbcak

def get_pages(channel):
    for i in range(1,100):
	get_page_from(channel,i)

get_page_from('http://www.mzitu.com/tag/zouguang',2)  


#if __name__='__main__':
#    start_url="http://www.mzitu.com/zhuanti"
#    callback=get_mei_channel(start_url)
#    for url in callback:
#	get_pages(url)
