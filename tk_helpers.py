import os
import numpy as np

from PIL import Image

def get_extension(f_name):
    return os.path.splitext(f_name)[1]

def load_image(path):
    return Image.open(path)

def load_images(path, ext=['.jpg']):
    imgs = []

    for image in os.listdir(path):
        if get_extension(image) not in ext: continue
        imgs.append(load_image(os.path.join(path, image)))

    return imgs

def resize_image(img, t_size):
    return img.resize(t_size)

def center_crop_img(img, t_size):
    o_width, o_height = img.size

    left, right = (o_width - t_size[0]) / 2, (o_width + t_size[0]) / 2
    top, bottom = (o_height - t_size[1]) / 2, (o_height + t_size[1]) / 2

    return img.crop((left, top, right, bottom))
