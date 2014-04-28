#coding: UTF-8
#-------------------------------------------------------------------------------
# Name:        高斯模糊算法
# Purpose:     直接操作像素，利用python具体实现
# Author:      leniy_tsan
# References:  http://en.wikipedia.org/wiki/Gaussian_blur
#
# Created:     2012-07-28
# Copyright:   (c) leniy_tsan 2012
# Licence:     GPL v2
#
# Note:        在图像域上，利用二维高斯矩阵进行卷积，既得高斯模糊
#              sigma为标准差；xy为两个方向上的矩阵宽度
#              可以分解为两个方向依次进行一维高斯矩阵卷积的卷积。
#-------------------------------------------------------------------------------
#!/usr/bin/env python
 
import numpy as np
import scipy.signal as signal
import sys, string
from PIL import Image
 
def gbm(R,sigma):
    # gaussian_blur_matrix
    #   R   为模糊半径
    # sigma 为标准差
    temp1=signal.gaussian(2*R+1,sigma)
    temp2=np.sum(temp1)  #用于归一化，使2R+1矩阵的和为1
    return temp1/temp2
 
def main(infile,outfile):
    #读取输入图像文件，并建立RGB数组
    ifp=Image.Image
    ifp=Image.open(infile)
    width,height=ifp.size
    matrixR=map(lambda _ : [0]*(height),range(width))#height行，width列
    matrixG=map(lambda _ : [0]*(height),range(width))
    matrixB=map(lambda _ : [0]*(height),range(width))
    for x in range(width):
        for y in range(height):
            matrixR[x][y]=ifp.getpixel((x,y))[0]
            matrixG[x][y]=ifp.getpixel((x,y))[1]
            matrixB[x][y]=ifp.getpixel((x,y))[2]
    del ifp
 
    #开始进行高斯卷积
    trans=gbm(3,2)
    trans_len=len(trans)
 
    #横向一维卷积，x方向
    blur_x_matrixR=map(lambda _ : [0]*(height),range(width))#height行，width列
    blur_x_matrixG=map(lambda _ : [0]*(height),range(width))
    blur_x_matrixB=map(lambda _ : [0]*(height),range(width))
    for x in range(width):
        for y in range(height):
            sum_xtempR=0
            sum_xtempG=0
            sum_xtempB=0
            for dx in range(trans_len):
                temp_x=x+dx-(trans_len-1)/2
                temp_y=y
                if temp_x >= 0:#超出图像边界的像素点，以0计算
                    if temp_x < width:
                        sum_xtempR += matrixR[temp_x][temp_y]*trans[dx]
                        sum_xtempG += matrixG[temp_x][temp_y]*trans[dx]
                        sum_xtempB += matrixB[temp_x][temp_y]*trans[dx]
            blur_x_matrixR[x][y]=sum_xtempR
            blur_x_matrixG[x][y]=sum_xtempG
            blur_x_matrixB[x][y]=sum_xtempB
 
    #在上述卷积结果上再次纵向一维卷积，y方向
    blur_xy_matrixR=map(lambda _ : [0]*(height),range(width))#height行，width列
    blur_xy_matrixG=map(lambda _ : [0]*(height),range(width))
    blur_xy_matrixB=map(lambda _ : [0]*(height),range(width))
    for y in range(height):
        for x in range(width):
            sum_ytempR=0
            sum_ytempG=0
            sum_ytempB=0
            for dy in range(trans_len):
                temp_y=y+dy-(trans_len-1)/2
                temp_x=x
                if temp_y >= 0:#超出图像边界的像素点，以0计算
                    if temp_y < height:
                        sum_ytempR += blur_x_matrixR[temp_x][temp_y]*trans[dy]
                        sum_ytempG += blur_x_matrixG[temp_x][temp_y]*trans[dy]
                        sum_ytempB += blur_x_matrixB[temp_x][temp_y]*trans[dy]
            blur_xy_matrixR[x][y]=sum_ytempR
            blur_xy_matrixG[x][y]=sum_ytempG
            blur_xy_matrixB[x][y]=sum_ytempB
 
    #生成输出图像文件
    ofp=Image.Image
    ofp=Image.new("RGB",(width,height))
    for x in range(width):
        for y in range(height):
            ofp.putpixel((x,y),(int(blur_xy_matrixR[x][y]),int(blur_xy_matrixG[x][y]),int(blur_xy_matrixB[x][y])))
    ofp.save(outfile)
    del ofp
 
main("test_in_01.jpg","test_out_01.jpg")#Leniy's Blog