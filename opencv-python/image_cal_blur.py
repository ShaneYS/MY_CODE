#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@application: 判断图像模糊程度
@creation time: 20190114
@modify time:
'''
# 参考网址：https://blog.csdn.net/qq_42238397/article/details/81745600
# 检测图片是否模糊有很多方法，比如FFT和variation of Laplacian等。
# FFT需要定义高频的量有多低和多高来区分图片是模糊的，比较麻烦；
# 而variation of Laplacian可以输出一个浮点数来代表图片的模糊程度。具体score值要根据自己数据确定




#######利用variation of Laplacian进行图像模糊检测#######
'''
Laplacian方法进行模糊判断的原理是Laplacian算子是用来衡量图片的二阶导，能够强调图片中密度快速变化的区域，也就是边界，故常用于边界检测。
在正常图片中边界比较清晰因此方差会比较大；而在模糊图片中包含的边界信息很少，所以方差会较小。
这个方法在opencv中只是一行代码的事：cv2.Laplacian(image_gray, cv2.CV_64F).var()
cv2.Laplacian前两个是必须参数：第一个参数是需要处理的图像；第二个参数是图像的深度，-1表示采用与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；
对于第二个参数的解释：https://blog.csdn.net/u010682375/article/details/70140803
'''
import cv2
import os
def varOfLaplacian(image_dir):
    '''
    :param image_dir:图像目录，其中存放彩色图像，用于批量测试
    :return:返回边缘方差，越大表示图像越清晰
    '''
    image_list = os.listdir(image_dir)
    for image in image_list:
        image_origin = cv2.imread(image_dir+image)
        image_gray = cv2.cvtColor(image_origin, cv2.COLOR_BGR2GRAY) #转为单通道的灰度图避免干扰
        edge_laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)
        # cv2.imshow('edge laplacian', edge_laplacian)
        # cv2.waitKey()
        score = edge_laplacian.var()
        print(score)

image_dir = '/home/ys/data/lpr/testImage/hard/blur/'
varOfLaplacian(image_dir)