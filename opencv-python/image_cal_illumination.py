#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@application: 判断图像亮度
@creation time: 20190119
@modify time:
'''

# 先把图片转换为灰度图,然后根据灰度值分布来判断
# 要判断图片的亮暗,只需要统计偏暗的像素个数,再除以图片像素的总个数,得到百分比p即可,至于p大于多少即判断为暗,则可以由你自己设置

from __future__ import print_function
import cv2, os, shutil, sys

def judgeIllumination(image_path, dark_dir, bright_dir, pixel_threshold=128, image_threshold=0.7, ):
    """
    :param image_path: 原始图像路径
    :param pixel_threshold: 像素阈值超参数，像素值低于此值则认为是暗像素
    :param image_threshold: 图像阈值超参数，dark_prop低于此值则认为是暗图像
    :param dark_dir: 保存暗图像的目录
    :param bright_dir: 保存亮图像的目录
    :return:
    """
    if not os.path.exists(dark_dir):
        os.mkdir(dark_dir)
        print('create dir: ', dark_dir)
    if not os.path.exists(bright_dir):
        os.mkdir(bright_dir)
        print('create dir: ', bright_dir)

    image = cv2.imread(image_path)
    #转为灰度图
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #获取灰度图矩阵的行数和列数
    rows, cols = image_gray.shape[:2]
    total_pixels = rows * cols #图像总像素数量
    dark_pixels = 0 #偏暗的像素数量，初始化为0个
    dark_prop = 0 #偏暗的像素占总像素比例，初始化为0

    #遍历灰度图的所有像素
    for row in image_gray:
        for col in row:
            if col < pixel_threshold:
                dark_pixels += 1
    dark_prop = dark_pixels / total_pixels
    print('total_pixels:{}, dark_pixels:{}, dark_prop:{}'.format(total_pixels, dark_pixels,dark_prop))

    if dark_prop > image_threshold:
        print(image_path + ' is dark.')
        shutil.copy(image_path, dark_dir)
    else:
        print(image_path + ' is bright.')
        shutil.copy(image_path, bright_dir)

if __name__ == '__main__':
    image_dir = '/home/ys/Github/opencv_prac/illumination/'
    dark_dir = '/home/ys/Github/opencv_prac/dark/'
    bright_dir = '/home/ys/Github/opencv_prac/bright/'
    image_list = os.listdir(image_dir)
    for image in image_list:
        image_path = image_dir + image
        pixel_threshold = sys.argv[1]
        image_threshold = sys.argv[2]
        pixel_threshold = int(pixel_threshold)
        image_threshold = float(image_threshold)
        judgeIllumination(image_path, dark_dir, bright_dir, pixel_threshold, image_threshold)