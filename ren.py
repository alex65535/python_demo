# coding=utf-8
import os
import sys
movie_name = os.listdir('.')
dup_name = '[电影天堂www.dy2018.com]'.decode(
    'utf-8').encode(sys.getfilesystemencoding())
for temp in movie_name:
    num = temp.find(dup_name)
    if num >= 0:
        newname = temp.replace(dup_name, "")
        print newname
        os.rename(temp,newname)
