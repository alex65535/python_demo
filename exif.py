#!/usr/bin/python3

import exifread  # pip install ExifRead
import datetime
import time
import os


def 通过exif_read读取(file_path):
    if not os.path.splitext(file_path)[1].lower() in ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif'):
        return
    f = open(file_path, 'rb')
    try:
        tags = exifread.process_file(f, stop_tag='DateTimeOriginal')
        创建日期字符串 = ""  # 2015:09:15 10:57:33
        if "EXIF DateTimeOriginal" in tags.keys():
            创建日期字符串 = tags["EXIF DateTimeOriginal"]
        elif "Image DateTime" in tags.keys():
            创建日期字符串 = tags["Image DateTime"]
        # print(创建日期字符串)

        a = list(str(创建日期字符串).replace(":", "").replace(" ", ""))
        文件路径 = file_path
        拍摄日期数据 = {}
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

        '''
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                print("Key: %s, value %s" % (tag, tags[tag]))
        '''
    finally:
        f.close()
    return


def 获取文件创建时间(file_path):
    t = os.path.getctime(file_path)
    timeStruct = time.localtime(t)
    print(time.strftime('%Y-%m-%d %H:%M:%S', timeStruct))
    a = list(time.strftime('%Y%m%d%H%M%S', timeStruct))
    文件路径 = file_path
    拍摄日期数据 = {}
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

#通过exif_read读取("E:\\未取得时间的文件 Note Pro\\IMG_20151215_112415.jpg")
#通过exif_read读取("G:\\Photos\\2015\\09\\15-09-15 10-57-33 3626.JPG")
#通过exif_read读取("Z:\\[备份]吴娜的 iPhone\\相册\\2015年12月\\IMG_0730.JPG")
#print(通过exif_read读取("Z:\\家庭照片视频\\手机备份\\anna手机备份 2015-03-19\\DCIM\\Camera\\20130822_212120.mp4")==None)
#print(通过exif_read读取("Z:\\家庭照片视频\\手机备份\\anna手机备份 2015-03-19\\DCIM\\Camera\\20130908_183713.jpG"))
print(获取文件创建时间("Z:\\家庭照片视频\\手机备份\\anna手机备份 2015-03-19\\DCIM\\Camera\\20130822_212120.mp4"))
