#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PIL import Image
def rename_file(path,cName):
    i = 0
    format_name = "jpg"
    format_name_after = "png"
    after_name = "rect_001_0_r5000"
    file_list = os.listdir(path)
    file_list.sort()
    for filename in file_list:
        #im = Image.open(path + filename)
        if filename.endswith(format_name):
            if (i < 10):
                print(path + filename, '=>', path + str(cName) + "00" + str(i) + "." + format_name_after)
                #os.rename(path + filename, path + str(cName) + "00" + str(i) + "." + fname_after)
                #os.rename(path + filename, path + "rect_001_" + str(i) + "_r5000" + "." + format_name_after)
            elif (i < 100):
                print(path + filename, '=>', path + str(cName) + "0" + str(i) + "." + format_name_after)
                #os.rename(path + filename, path + str(cName) + "0" + str(i) + "." + fname_after)
                #os.rename(path + filename, path + after_name + "00" + str(i) + "." + format_name_after)
                #os.rename(path + filename, path + "rect_001_" + str(i) + "_r5000" + "." + format_name_after)
            else:
                print(path + filename, '=>', path + str(cName) + str(i) + "." + format_name_after)
                #os.rename(path + filename, path + str(cName) + str(i) + "." + fname_after)
                #os.rename(path + filename, path + after_name + "0" + str(i) + "." + format_name_after)
                #os.rename(path + filename, path + "rect_001_" + str(i) + "_r5000" + "." + format_name_after)
            i += 1
            #im.save("/home/git/tmpdataset/Rectified/scan1_train/" + filename.split(".")[0] + "." + fname_after)
            im.save("/home/git/tmpdataset/Rectified/scan1_train/" + filename + "." + fname_after)
rename_file("/home/git/tmpdataset/ex/","0000")
