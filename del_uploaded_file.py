#!/usr/bin/python3

'''
删除目录中对应的已上传的文件
'''

import shutil,os
import sys
import io
import re
import random
import datetime
import time
import get_media_create_time

##
照片视频文件目录路径 = "Y:\\XiaoMi\\家庭照片视频\\专题"
目标目录路径 = "G:\\Photos"
未获得时间的文件保存目录路径 = "E:\\未取得时间的文件 家庭照片视频"
未获得媒体创建时间时使用文件创建时间 = False
##

def 保证目录路径最后是斜杠(foldpath):
    if foldpath[-1] != "\\":
        foldpath = foldpath + "\\"
    return foldpath

照片视频文件目录路径 = 保证目录路径最后是斜杠(照片视频文件目录路径)
目标目录路径 = 保证目录路径最后是斜杠(目标目录路径)
未获得时间的文件保存目录路径 = 保证目录路径最后是斜杠(未获得时间的文件保存目录路径)

已经复制的文件路径列表 = []
已复制文件列表文件路径 = 照片视频文件目录路径 + "copyed.txt"
记录未找出创建时间的文件路径 = 照片视频文件目录路径 + "untime.txt"

def 移动文件(文件名和日期信息):
    当前文件目标目录路径 = 目标目录路径 + 文件名和日期信息["拍摄日期"]["四位年"] \
        + "\\" + 文件名和日期信息["拍摄日期"]["月"]+"\\"
    #print(当前文件目标目录路径)
    if os.path.exists(当前文件目标目录路径) != True:
        os.makedirs(当前文件目标目录路径)
    新文件路径 = 当前文件目标目录路径+文件名和日期信息["拍摄日期"]["文件名"]
    if os.path.exists(新文件路径):
        print("存在文件："+ 新文件路径)
        os.remove(新文件路径)
    #shutil.copy(文件名和日期信息["文件名"],当前文件目标目录路径+文件名和日期信息["拍摄日期"]["文件名"])
    保存已复制的文件路径到记录文件(文件名和日期信息["文件名"])
    return

def 保存已复制的文件路径到记录文件(filepath):
    return
    f = open(已复制文件列表文件路径,'a')
    try:
        f.write("\n"+ filepath)
    finally:
        f.close()

def 保存未解析出时间的文件(filepath):
    return
    f = open(记录未找出创建时间的文件路径,'a')
    try:
        f.write("\n"+ filepath)
    finally:
        f.close()

def 复制未取得创建时间的文件到指定目录(filepath):
    return
    目标文件路径 = 未获得时间的文件保存目录路径+os.path.split(filepath)[1]
    if os.path.exists(目标文件路径):
        a = os.path.splitext(os.path.split(filepath)[1])
        目标文件路径 = 未获得时间的文件保存目录路径+ a[0] + "__" + str(random.randint(100,999)) + a[1]
    shutil.copy(filepath, 目标文件路径)
    #print(filepath, 目标文件路径)

def 找出所有图片视频和拍摄信息():
    文件总数 = 0
    for find_obj in os.walk(照片视频文件目录路径):
        #print(i[0],"\n##",i[1],"\n##",i[2])
        文件总数 = 文件总数 + len(find_obj[2])
    print("文件总数： " + str(文件总数))

    正在处理的文件 = 0
    未解析出时间的文件数量 = 0
    #for filename in 图片视频列表:
    for find_obj in os.walk(照片视频文件目录路径):
        当前目录路径 = find_obj[0]
        当前目录路径 = 保证目录路径最后是斜杠(当前目录路径)
        for filename in find_obj[2]:
            正在处理的文件 = 正在处理的文件 + 1
            print("正在处理的文件" + str(正在处理的文件)+"/" + str(文件总数) + "："+ 当前目录路径 + filename)
            if filename=="copyed.txt":
                continue
            if filename=="untime.txt":
                continue
            文件名和日期信息 = {"文件名": "", "拍摄日期": ""}
            文件名和日期信息["文件名"] = 当前目录路径 + filename
            if 文件名和日期信息["文件名"] in 已经复制的文件路径列表 :
                continue
            文件名和日期信息["拍摄日期"] = get_media_create_time.获取图片视频的拍摄时间数据(文件名和日期信息["文件名"], 未获得媒体创建时间时使用文件创建时间)
            if 文件名和日期信息["拍摄日期"] == None:
                未解析出时间的文件数量 = 未解析出时间的文件数量 + 1
                保存未解析出时间的文件(文件名和日期信息["文件名"])
                复制未取得创建时间的文件到指定目录(文件名和日期信息["文件名"])
                continue
            移动文件(文件名和日期信息)
    print("未解析出时间的文件数量: " + str(未解析出时间的文件数量))

def 读取所有已复制的文件():
    return
    if os.path.exists(已复制文件列表文件路径):
        file_object = open(已复制文件列表文件路径) #不要把open放在try中，以防止打开失败，那么就不用关闭了
        try:
            global 已经复制的文件路径列表
            #file_context = file_object.read() #file_context是一个string，读取完后，就失去了对test.txt的文件引用
            已经复制的文件路径列表 = file_object.read().splitlines() 
            #file_context是一个list，每行文本内容是list中的一个元素
        finally:
            file_object.close()

读取所有已复制的文件()
找出所有图片视频和拍摄信息()
