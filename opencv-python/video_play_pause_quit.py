#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@creation time: 2019/01/06 20:40
@modify time:
'''

import cv2
video_path = '/home/ys/LPR/testData/video/cut11_2.webm'
cap = cv2.VideoCapture(video_path)

# 采用while循环，逐帧读取视频
while cap.isOpened():
    suc, frame = cap.read()

    if not suc:
        break

    cv2.imshow('current frame', frame)

    # 延时1ms 等待按键按下
    key = cv2.waitKey(1) & 0xFF #0xFF为16进制的11111111,防止在某些平台出现bug
    if key == ord(' '):
        cv2.waitKey(0)
    elif key == 27: # 用esc退出，也可改为其他，如用q退出：key == ord('q')
        break

# 必要代码，释放视频缓存，关闭打开的图像窗口，没有会报错
cap.release()
cv2.destroyAllWindows()