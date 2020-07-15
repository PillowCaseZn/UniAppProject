#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author      : PillowCase
# Create Time : 2020-05-13 12:51
# Description : 生成不同尺寸的Iocn素材
# Python 2.7

import os
from PIL import  Image

folder = "F:/Project/UniAppProject/Icon"

image_data = [
	['drawable',  512],
	['drawable-ldpi' , 36],
	['drawable-mdpi' , 48],
	['drawable-hdpi' , 72],
	['drawable-xhdpi' , 96],
	['drawable-xxhdpi' , 144],
	['drawable-xxxhdpi' , 192]
]

image_file = [
	'icon.png',
	'push.png',
	'splash.png'
]

def createImage(size):
    im = Image.open(imageDirectory+"/icon.png")
    im.resize((size,size), Image.ANTIALIAS).save(imageDirectory+"/icon.png")


for data  in image_data:
	for img in image_file:
		img_path = '%s/%s' % (folder ,img)
		if os.path.exists(img_path):
			im = Image.open(img_path)
			img_folder = '%s/%s' % ( folder , data[0])
			if os.path.exists(img_folder) is False:
				os.mkdir(img_folder)
			im.resize((data[1] , data[1]), Image.ANTIALIAS).save('%s/%s' % (img_folder , img))


