#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@application: python多线程，以爬虫（通过豆瓣API抓取30部影片信息）为例。
@creation time: 20190106
@modify time:
'''

'''
python3中，由于thread有两个很致命的问题，所以python3更推荐用threading代替thread，thread被改名为_thread

urllib是Python中请求url连接的官方标准库。
python2中，urllib和urllib2都是接受URL请求的相关模块，但是提供了不同的功能。
在Python3中整合成了urllib。urllib3则是增加了连接池等功能，两者互相都有补充的部分。
'''
# URL：统一资源定位符，Uniform Resource Locator



image_dir = '/home/ys/Github/MY_CODE/prac/images/'
load_and_resize(image_dir)

if __name__ == '__main__':
    import glob, os, cv2
    from threading import Thread
    import urllib.request, time

    start_time = time.time()
    url = 'https://movie.douban.com/top250'
    n = 5
    t = Thread(target=task, args=(url, n))
    t.start()
    print(time.time()-start_time)