import shutil,os
import sys
import io
import re
import random
import datetime
import time
import random

文件列表文件路径 = "Z:\\[备份]钱锋的 iPhone\\untime.txt"
未获得时间的文件保存目录路径 = "E:\\bb\\"

def 保证目录路径最后是斜杠(foldpath):
    if foldpath[-1] != "\\":
        foldpath = foldpath + "\\"
    return foldpath

b = "c:\\a"
print(保证目录路径最后是斜杠(b))
print(b)
exit(1)

def 读取未取得时间的文件():
    if os.path.exists(文件列表文件路径):
        file_object = open(文件列表文件路径) #不要把open放在try中，以防止打开失败，那么就不用关闭了
        try:
            #file_context = file_object.read() #file_context是一个string，读取完后，就失去了对test.txt的文件引用
            需要复制文件路径列表 = file_object.read().splitlines() 
            需要复制的文件总数 = len(需要复制文件路径列表)
            print("需要复制文件总数：" + str(需要复制的文件总数))
            正在处理文件序号 = 0
            for filepath in 需要复制文件路径列表:
                正在处理文件序号 = 正在处理文件序号 + 1
                print("正在处理文件序号: " + str(正在处理文件序号) + "/" + str(需要复制的文件总数))
                if (filepath!=""):
                    复制未取得创建时间的文件到指定目录(filepath)
        finally:
            file_object.close()

def 复制未取得创建时间的文件到指定目录(filepath):
    目标文件路径 = 未获得时间的文件保存目录路径+os.path.split(filepath)[1]
    if os.path.exists(目标文件路径):
        a = os.path.splitext(os.path.split(filepath)[1])
        目标文件路径 = 未获得时间的文件保存目录路径+ a[0] + "__" + str(random.randint(100,999)) + a[1]
    shutil.copy(filepath, 目标文件路径)
    #print(filepath, 目标文件路径)


读取未取得时间的文件()