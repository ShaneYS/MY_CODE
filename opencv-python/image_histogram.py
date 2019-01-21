#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@application: 计算灰度图像直方图，直方图均衡化，直方图规定化，局部直方图
@creation time: 20190119
@modify time:
'''

#参考https://blog.csdn.net/YZXnuaa/article/details/79231817
'''
opencv的cv2.calcHist函数有五个参数：
    image：输入图像，传入时应该用中括号[]括起来
    channels:传入图像的通道。如果是灰度图像，那就只有一个通道，值为0；如果是彩色图像（3通道），那么值为0,1,2中选择一个，对应着BGR各个通道。这个值也用[]传入。
    mask：掩膜图像。如果统计整幅图，那么为None。主要是如果要统计部分图的直方图，就得构造相应的炎掩膜来计算。
    histSize：灰度级的个数，需要中括号，比如[256]
    ranges:像素值的范围，通常[0,256]，有的图像如果不是0-256，比如说你来回各种变换导致像素值负值、很大，则需要调整后才可以。
'''

def calcHist(image_path):
    image_gray = cv2.imread(image_path, 0)
    hist = cv2.calcHist([image_gray], [0], None, [256], [0,256])
    plt.subplot(121), plt.imshow(image_gray, 'gray')
    plt.subplot(122), plt.plot(hist)
    plt.show()

if __name__ == '__main__':
    import cv2
    import matplotlib.pyplot as plt
    image_path = '/home/ys/Github/opencv_prac/1.jpg'
    calcHist(image_path)
