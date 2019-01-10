#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@creation time: 20190110
@modify time:
'''

#src:source，源; dst:destination，目的;
#opencv的shape函数返回的是（行数，列数，通道数），即（高度，宽度，通道数）


import cv2
import numpy as np
import matplotlib.pyplot as plt




#######显示图片#######
def showImage(input, output):
    plt.subplot(121), plt.imshow(input), plt.title('input')
    plt.subplot(122), plt.imshow(output), plt.title('output')
    plt.show()




#######仿射变换 affine transform#######
def affineTransform(image, src, dst):
    rows, cols, ch = image.shape
    matrix = cv2.getAffineTransform(src, dst)
    result = cv2.warpAffine(image, matrix, (cols,rows))
    return result

# image_path = '/home/ys/Github/opencv_prac/1.jpg'
# image = cv2.imread(image_path)
# src = np.float32([[50,50], [200,50], [50,200]])
# dst = np.float32([[10,100], [200,50], [50,200]])
# result = affineTransform(image, src, dst)
# showImage(image, result)




#######透视变换 prespective transform#######
def perspectiveTransform(image, src, dst):
    rows, cols, ch = image.shape
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(image, matrix, (cols,rows))
    return result

# image_path = '/home/ys/Github/opencv_prac/1.jpg'
# image = cv2.imread(image_path)
# src = np.float32([[56,65], [368,52], [28,387], [389,390]])
# dst = np.float32([[0,0], [300,0], [0,300], [300,300]])
# result = perspectiveTransform(image, src, dst)
# showImage(image, result)




#######颜色空间变换 convert color#######
# 颜色转换可以使用cv2.cvtColor(input_image,flag)，其中flag确定了转换的类型。还可以在读取图片时就转为灰度图
# OpenCV中有274多种颜色空间转换方法,最广泛使用的两个:BGR2GRAG和BGR2HSV。
# 将RGB转为灰度图，使用flag:cv2.COLOR_BGR2GRAY。将RGB转为HSV，使用flag：cv2.COLOR_BGR2HSV
def getAllFlag():
    #查看opencv中所有颜色空间变换的flag
    import cv2
    flags = []
    for i in dir(cv2):
        if i.startswith('COLOR_'):
            flags.append(i)
    print(len(flags), flags)
# getAllFlag()

def bgr2gray(image):
    # OpenCV对RGB图像数据的存储顺序是BGR
    result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return result

def bgr2hsv(image):
    result = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return result

# image_path = '/home/ys/Github/opencv_prac/1.jpg'
# image = cv2.imread(image_path)
# gray = bgr2gray(image)
# hsv = bgr2hsv(image)
# gray = cv2.resize(gray, (500,500))
# hsv = cv2.resize(hsv, (500,500))
# cv2.imshow('gray', gray)
# cv2.imshow('hsv', hsv)
#
# # 在读取图片时就转为灰度图。使用cv2.imread()读入图片，共两个参数。第一个参数为要读入的图片文件名。第二个参数指定图片的读取方式。
# cv2.IMREAD_COLOR : 默认使用该种标识。加载一张彩色图片，忽视它的透明度。1
# cv2.IMREAD_GRAYSCALE : 加载一张灰度图。0
# cv2.IMREAD_UNCHANGED : 加载图像，包括它的Alpha通道。-1
# image_path = '/home/ys/Github/opencv_prac/1.jpg'
# img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# cv2.imwrite('/home/ys/Github/opencv_prac/1_gray.jpg', img_gray)
# img_gray = cv2.resize(img_gray, (500,500))
# cv2.imshow('gray2', img_gray)
# cv2.waitKey()

#灰度图转为二值图：全局阈值
# image_gray = cv2.imread('/home/ys/Github/opencv_prac/1.jpg', 0)
# #使用cv2.imshow和plt.show显示颜色不同，因为opencv使用的是BGR，而plt使用的是RGB。故最好使用opencv显示
# ret, boundary = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY)
# cv2.imwrite('/home/ys/Github/opencv_prac/1_boundary.jpg', boundary)

#灰度图转为二值图：自适应阈值
# image = cv2.imread('/home/ys/Github/opencv_prac/1.jpg')
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# image_boundary = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imshow('boundary', image_boundary)
# cv2.waitKey()




#######弹性变换 elastic transform#######
