#coding=utf-8
#!/usr/bin/python

from glob import glob
#pip install Pillow
from PIL import Image, ImageDraw, ImageFont
import os
import math

#Origin file catalog  
SORUCE_DIR = 'E:/Python project/01Origin pictures'
#File catalog after processing
TARGET_DIR= 'E:/Python project/02Compressed pictures'
#Picture screening condition
THRESHOLD = 100000  #100kb
#Limitation of height/width
NEW_W_H = 800
#whether show mark
WAHTER_MARK = 0  

FONT_FAMILY = 'C:/Windows/Fonts/constan.ttf'

def add_text_to_image(image, text, font_size, font_family=FONT_FAMILY):
    width, height = image.size
    img_draw = ImageDraw.Draw(image)
    Font = ImageFont.truetype(font_family, font_size)  
    textW,textH = Font.getsize(text)   
    pointX = width - textW - textH / 2
    pointY = height - textH - textH / 2
    img_draw.text([pointX, pointY], text, fill=(255, 255, 255, 100), font = Font)


def resize_images(source_dir, target_dir, threshold, new_w_or_h):
    filenames = glob('{}/*'.format(source_dir))
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for filename in filenames:
        filesize = os.path.getsize(filename)
        if filesize >= threshold:
            with Image.open(filename) as im:
                width, height = im.size
                if width >= height:
                    new_width = new_w_or_h
                    new_height = int(new_width * height * 1.0 / width)
                else:
                    new_height = new_w_or_h
                    new_width = int(new_height * width * 1.0 / height)
                resized_im = im.resize((new_width, new_height))
                if WAHTER_MARK != 0:
                    add_text_to_image(resized_im, "dp2px.com", int(new_w_or_h / 30))
                output_filename = filename.replace(source_dir, target_dir)
                resized_im.save(output_filename)
    print('Picture processing finalized!')

resize_images(SORUCE_DIR, TARGET_DIR, THRESHOLD, NEW_W_H)
