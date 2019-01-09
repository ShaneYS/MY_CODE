#!/usr/bin/env python
# coding: utf-8

'''
@author: YangShuai
@category: opencv-python
@creation time: 2019/01/09
@modify time:
'''
import cv2

# 加载视频文件
video_path = '/home/ys/LPR/testData/video/cut11_2.webm'
cap = cv2.VideoCapture(video_path)

# 设置视频保存的参数
save_name = video_path.strip('\'').split('/')[-1].split('.')[0] + '_result' + '.avi' #avi文件适用于各种平台
# Four-Character Codes,控制视频编码格式,设置的不合适则生成的视频为0K。
# 若设置为-1，程序运行时则会交互地弹出一个对话框让你从系统已有的编码中选择一个.
# cv2.VideoWriter_fourcc()函数的作用是输入四个字符代码即可得到对应的视频编码器。
fourcc = cv2.VideoWriter_fourcc(*'XVID') # 使用XVID编码器及avi格式是最通用的视频方案
# fps = cap.get(cv2.CAP_PROP_FPS) # 但是这个函数对于webm视频返回的是1000，原因不明
fps = 24
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter(save_name, fourcc, fps, size) # 四个参数：保存文件名、编码器、帧率、视频宽高


# 采用while循环，逐帧读取视频
while cap.isOpened():
    suc, frame = cap.read()

    if not suc:
        break

    frame_filp = cv2.flip(frame, 0)
    cv2.imshow('current frame', frame_filp)

    # 延时1ms 等待按键按下
    key = cv2.waitKey(1) & 0xFF #0xFF为16进制的11111111,防止在某些平台出现bug
    if key == ord(' '):
        cv2.waitKey(0)
    elif key == 27: # 用esc退出，也可改为其他，如用q退出：key == ord('q')
        break
    out.write(frame_filp)

# 必要代码，释放视频缓存，关闭打开的图像窗口，没有会报错
cap.release()
out.release()
cv2.destroyAllWindows()