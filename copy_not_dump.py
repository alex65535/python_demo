#!/usr/bin/python3

# 复制源目录文件到目标目录
import shutil
import os

源文件目录路径 = "E:\\b"
目标目录路径 = "G:\\Photos"
'''
源文件目录路径 = "E:\\a"
目标目录路径 = "E:\\bb"
'''

if 源文件目录路径[-1] != "\\":
    源文件目录路径 = 源文件目录路径 + "\\"

if 目标目录路径[-1] != "\\":
    目标目录路径 = 目标目录路径 + "\\"

文件总数 = 0
for find_obj in os.walk(源文件目录路径):
    # print(i[0],"\n##",i[1],"\n##",i[2])
    文件总数 = 文件总数 + len(find_obj[2])
print("文件总数： " + str(文件总数))

正在处理的文件 = 0

for find_obj in os.walk(源文件目录路径):
    当前目录路径 = find_obj[0]
    if 当前目录路径[-1] != "\\":
        当前目录路径 = 当前目录路径 + "\\"
    当前源文件的相对目录路径 = 当前目录路径.replace(源文件目录路径, "")
    for filename in find_obj[2]:
        正在处理的文件 = 正在处理的文件 + 1
        当前文件路径 = 当前目录路径 + filename
        当前文件目标文件路径 = 目标目录路径 + 当前源文件的相对目录路径 + filename
        print("正在处理的文件" + str(正在处理的文件)+"/" + str(文件总数) + "："+当前文件路径)
        #print(当前文件路径, 当前文件目标文件路径)
        if not os.path.exists(目标目录路径 + 当前源文件的相对目录路径):
            os.makedirs(目标目录路径 + 当前源文件的相对目录路径)
        if not os.path.exists(当前文件目标文件路径):
            shutil.copy(当前文件路径, 当前文件目标文件路径)
        else:
            print("已存在")
