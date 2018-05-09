import exifread #pip install ExifRead

def exif_read读取(file_path):
    f = open(file_path, 'rb')
    try:
        tags = exifread.process_file(f, stop_tag='DateTimeOriginal')
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                print("Key: %s, value %s" % (tag, tags[tag]))
    finally:
        f.close()
    return

#exif_read读取("E:\\未取得时间的文件 Note Pro\\IMG_20151215_112415.jpg")
exif_read读取("G:\\Photos\\2015\\09\\15-09-15 10-57-33 3626.JPG")