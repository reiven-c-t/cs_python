#!/usr/bin/env python

'''
=======================
From the MNIST Website:
=======================

TRAINING SET IMAGE FILE (train-images-idx3-ubyte):

[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000803(2051) magic number 
0004     32 bit integer  60000            number of images 
0008     32 bit integer  28               number of rows 
0012     32 bit integer  28               number of columns 
0016     unsigned byte   ??               pixel 
0017     unsigned byte   ??               pixel 
........ 
xxxx     unsigned byte   ??               pixel
Pixels are organized row-wise. 
Pixel values are 0 to 255.
0 means background (white), 255 means foreground (black).

TRAINING SET LABEL FILE (train-labels-idx1-ubyte):

[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000801(2049) magic number (MSB first) 
0004     32 bit integer  60000            number of items 
0008     unsigned byte   ??               label 
0009     unsigned byte   ??               label 
........ 
xxxx     unsigned byte   ??               label
The labels values are 0 to 9.
'''

import numpy as np
from PIL import Image
import json, os
from collections import OrderedDict

training_images = list()
training_lbls = OrderedDict()

SIZE = 28

with open('train-images.idx3-ubyte', 'rb') as train_imgs_file:
    train_imgs_file.read(16)
    for i in range(60000):
        print('Image #%s' % (i + 1), end='\r')
        new_image = np.zeros((SIZE, SIZE))
        for row in range(SIZE):
            for col in range(SIZE):
                new_image[row][col] = 0 if (255 - int.from_bytes(train_imgs_file.read(1), 'big') > 127) else 1

        training_images.append(new_image)

print('Done reading training images, now to write...')

if not os.path.exists('training-images/'):
    os.mkdir('training-images')

if not os.path.exists('train/'):
    os.mkdir('train')

control = True
with open('train-labels.idx1-ubyte', 'rb') as train_lbls_file:
    train_lbls_file.read(8)
    for idx, img in enumerate(training_images):
        train_img_name = 'training-images/mnist-image-%d.csv' % idx
        print('Image #%s' % (idx + 1), end='\r')
        training_lbls[train_img_name] = int.from_bytes(train_lbls_file.read(1), 'big')
        if control:
            print(img)
            print(type(img))
            control = False
        np.int8(img)
        label_folder = training_lbls[train_img_name]
        folder_path = 'train/%d/' % label_folder
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        train_img_name = folder_path + '/img-%d.csv' % idx
        np.savetxt(train_img_name, img, delimiter=',', fmt="%1d")
        # Image.fromarray(img).convert('RGB').save(train_img_name)

# with open('training-labels.json', 'w') as train_lbls_json:
#     json.dump(training_lbls, train_lbls_json)

print('Done.')
