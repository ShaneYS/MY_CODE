#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@application: 进程池加速Python数据处理
@creation time: 20190119
@modify time:
'''

# 参考：https://zhuanlan.zhihu.com/p/45833152


# import glob
# import os
# import cv2
#
# os.chdir('./images/')
# a = glob.glob('*.jpg')
# print(type(a), len(a))
# for image_filename in glob.glob("*.jpg"):
#     img = cv2.imread(image_filename)
#     img = cv2.resize(img, (600, 600))
#     cv2.imwrite('/home/ys/Github/MY_CODE/prac/resize/'+image_filename, img)


import glob, os, cv2
import concurrent.futures
def load_and_resize(image_filename):
    img = cv2.imread(image_filename)
    img = cv2.resize(img, (600, 600))
    cv2.imwrite('/home/ys/Github/MY_CODE/prac/resize/'+image_filename, img)

### Create a pool of processes. By default, one is created for each CPU in your machine.
with concurrent.futures.ProcessPoolExecutor() as executor:
    os.chdir('./images/')
    image_files = glob.glob("*.jpg")
 ### Process the list of files, but split the work across the process pool to use all CPUs
    executor.map(load_and_resize, image_files)
