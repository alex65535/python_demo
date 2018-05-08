import shutil,os
import sys
import io
import re
import random
import datetime
import time
import hachoir #pip install hachoir3==3.0a2
#from hachoir import core
from hachoir import metadata
from hachoir import parser
#from hachoir import stream
#from hachoir import subfile

照片视频文件目录路径 = 'Z:\\家庭照片视频\\手机备份\\simon手机备份 2015-5-10\\DCIM\\Camera\\'
照片视频文件目录路径 = "e:\\a\\"
#照片视频文件目录路径 = "C:\\Camera\\"
目标目录路径 = "e:\\b\\"
已经复制的文件路径列表 = []
已复制文件列表文件路径 = 照片视频文件目录路径 + "copyed.txt"
记录未找出创建时间的文件路径 = 照片视频文件目录路径 + "untime.txt"

def 获取图片视频的拍摄时间数据(文件路径):
    parserFile = parser.createParser(文件路径)  # 解析文件
    if not parserFile:
        #print("Unable to parse file - {}\n".format(file))
        return ""
    try:
        metadataDecode = metadata.extractMetadata(parserFile)  # 获取文件的metadata
        # print(metadataDecode)
    except ValueError:
        #print('Metadata extraction error.')
        metadataDecode = None
        return ""

    if not metadataDecode:
        #print("Unable to extract metadata.")
        return ""

    myList = metadataDecode.exportPlaintext(
        line_prefix="")  # 将文件的metadata转换为list,且将前缀设置为空

    # print(myList)
    视频MIMEType = "MIME type: video/"
    创建日期tag = 'Creation date: '

    是视频 = "".join(myList).find(视频MIMEType) > -1

    拍摄日期数据 = {}
    for i in range(1, len(myList)+1):
        # 如果字符串在列表中,则提取数字部分,即为文件创建时间
        if 创建日期tag in myList[i-1]:
            创建时间字符串 = myList[i-1].replace(创建日期tag, "")
            创建时间 = datetime.datetime.strptime(创建时间字符串, '%Y-%m-%d %H:%M:%S')
            # print(创建时间)
            if 是视频:
                创建时间 = 创建时间 + datetime.timedelta(hours=8)
            # print(创建时间.strftime("%Y%m%d%H%M%S"))
            # fileTime = re.sub(r"\D", '', myList[i-1])  # 使用正则表达式将列表中的非数字元素剔除
            a = list(创建时间.strftime("%Y%m%d%H%M%S"))  # 将文件创建时间字符串转为列表list
            拍摄日期数据["四位年"] = "".join(a[0:4])
            拍摄日期数据["二位年"] = "".join(a[2:4])
            拍摄日期数据["月"] = "".join(a[4:6])
            拍摄日期数据["日"] = "".join(a[6:8])
            拍摄日期数据["时"] = "".join(a[8:10])
            拍摄日期数据["分"] = "".join(a[10:12])
            拍摄日期数据["秒"] = "".join(a[12:14])
            拍摄日期数据["文件名"] = 拍摄日期数据["二位年"] + "-" + 拍摄日期数据["月"] + \
                "-"+拍摄日期数据["日"] + " "+拍摄日期数据["时"]+"-"+拍摄日期数据["分"]+"-"+拍摄日期数据["秒"] +\
                " " + str(os.path.getsize(文件路径))[-4:]+os.path.splitext(文件路径)[1]
            # a.insert(timePosition, '_')  # 将列表插入下划线分割date与time
            # fileFinalTime = "".join(a)  # 重新将列表转为字符串

            #print("The {0} is: {1}".format(myChar, fileFinalTime))
            return 拍摄日期数据
    return ""


def 移动文件(文件名和日期信息):
    当前文件目标目录路径 = 目标目录路径 + 文件名和日期信息["拍摄日期"]["四位年"] \
        + "\\" + 文件名和日期信息["拍摄日期"]["月"]+"\\"
    #print(当前文件目标目录路径)
    if os.path.exists(当前文件目标目录路径) != True:
        os.makedirs(当前文件目标目录路径)
    shutil.copy(文件名和日期信息["文件名"],当前文件目标目录路径+文件名和日期信息["拍摄日期"]["文件名"])
    保存已复制的文件路径到记录文件(文件名和日期信息["文件名"])
    return

def 保存已复制的文件路径到记录文件(filepath):
    f = open(已复制文件列表文件路径,'a')
    try:
        f.write("\n"+ filepath)
    finally:
        f.close()

def 保存未解析出时间的文件(filepath):
    f = open(记录未找出创建时间的文件路径,'a')
    try:
        f.write("\n"+ filepath)
    finally:
        f.close()

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
        if 当前目录路径[-1]!="\\":
            当前目录路径 = 当前目录路径 + "\\"
        for filename in find_obj[2]:
            正在处理的文件 = 正在处理的文件 + 1
            print("正在处理的文件" + str(正在处理的文件)+"/" + str(文件总数) + "："+filename)
            if filename=="copyed.txt":
                continue
            if filename=="untime.txt":
                continue
            文件名和日期信息 = {"文件名": "", "拍摄日期": ""}
            文件名和日期信息["文件名"] = 当前目录路径 + filename
            if 文件名和日期信息["文件名"] in 已经复制的文件路径列表 :
                continue
            文件名和日期信息["拍摄日期"] = 获取图片视频的拍摄时间数据(文件名和日期信息["文件名"])
            if 文件名和日期信息["拍摄日期"] == "":
                未解析出时间的文件数量 = 未解析出时间的文件数量 + 1
                保存未解析出时间的文件(文件名和日期信息["文件名"])
                continue
            移动文件(文件名和日期信息)
    print("未解析出时间的文件数量: " + str(未解析出时间的文件数量))

def 读取所有已复制的文件():
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
