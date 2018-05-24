# -*- coding: utf-8 -*-
"""
Created on Mon May  7 18:43:55 2018

@author: susmote
"""

# coding = utf-8

import requests
import random
import re
from lxml import etree

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"]

baseUrl = { "ChinaMale"  : "http://www.manmankan.com/dy2013/mingxing/neidi/nanmingxing.shtml",
			"ChinaFemale": "http://www.manmankan.com/dy2013/mingxing/neidi/nvmingxing.shtml",
			"EuroMale"   : "http://www.manmankan.com/dy2013/mingxing/oumei/nanmingxing.shtml",
			"EuroFemale" : "http://www.manmankan.com/dy2013/mingxing/oumei/nvmingxing.shtml"}

basePicUrl = "http://www.manmankan.com/dy2013/mingxing/tupian"
localPath = r"E:\susmote\Documents/"

order = 0

def makeHeader():
    user_agent = random.choice(USER_AGENTS)
    headers = {'user_agent': user_agent, "referer": "http://www.manmankan.com/dy2013/mingxing/"}
    return headers


def doRequests(Url,timeout=5):
    header = makeHeader()
    print("Now downloading Url:  " + Url)
    try:
        resp = requests.get(Url, headers=header, timeout=timeout)
        if resp.status_code == 200:
            return resp
        else:
            return None
    except:
        print("Error at :  " + Url)
        return  None

def getPicURL(url,timeout = 15):
    header = makeHeader()
    resp = doRequests(url,timeout=timeout)
    if resp != None:
        content = etree.HTML(resp.text)
        suffix = makeSuffix(content)
        picUrl = makePicUrl(suffix)
        return picUrl
    else:
        print ("Erro at getPicURL!")
        return None


def makeSuffix(html,num=500):
    href = html.xpath("//div[@id='listCont']//div[@class='i_cont_s']//a/@href")
    suffix = []
    pattern = re.compile('/\d+/\d+.shtml')
    for i in href:
        suffix.append(pattern.findall(i)[0])
    return suffix[:num]

def makePicUrl(suffix):
    picUrl = []
    for i in suffix:
        picUrl.append(basePicUrl+i)
    return picUrl


def getImg(picURL,timeout = 20):
    for url in picURL:
        resp = doRequests(url,timeout=timeout)
        if resp == None:
            continue
        html = etree.HTML(resp.text)
        rowUrl = html.xpath("//div[@class='main_p']//ul//li//a//img/@data-original")
        imgUrl = []
        for i in rowUrl:
            imgUrl.append(i.replace("_s",""))

        num = 50 if len(imgUrl) > 50 else len(imgUrl)
        num = num/2
        global order  # need fix
        order += 1  # need fix
        num = int(num)
        for i in range(num):
            url = imgUrl[i]
            resp = doRequests(url,timeout=10)
            if resp == None:
                continue
            img = resp.content
            if img == None:
                continue
            imgName = str(order)+"_"+str(i)+".jpg"
            try:
                img_resourse = open(localPath + imgName, 'wb')
                img_resourse.write(img)
            except:
                print("Error at writing!")



def Crawl(key):
    target = baseUrl[key]
    picUrl = getPicURL(target)
    getImg(picUrl)

if __name__ == '__main__':
    Crawl("ChinaMale")
