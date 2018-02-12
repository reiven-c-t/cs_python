#!/usr/bin/env python

'''
=======================
From the MNIST Website:
=======================

TEST SET IMAGE FILE (t10k-images-idx3-ubyte):

[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000803(2051) magic number 
0004     32 bit integer  10000            number of images 
0008     32 bit integer  28               number of rows 
0012     32 bit integer  28               number of columns 
0016     unsigned byte   ??               pixel 
0017     unsigned byte   ??               pixel 
........ 
xxxx     unsigned byte   ??               pixel
Pixels are organized row-wise.
Pixel values are 0 to 255.
0 means background (white), 255 means foreground (black). 

TEST SET LABEL FILE (t10k-labels-idx1-ubyte):

[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000801(2049) magic number (MSB first) 
0004     32 bit integer  10000            number of items 
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

testing_images = list()
testing_lbls = OrderedDict()


SIZE = 28

with open('t10k-images.idx3-ubyte', 'rb') as test_imgs_file:
    test_imgs_file.read(16)
    for i in range(10000):
        print('Image #%s' % (i + 1), end='\r')
        new_image = np.zeros((SIZE, SIZE))
        for row in range(SIZE):
            for col in range(SIZE):
                new_image[row][col] = 0 if (255 - int.from_bytes(test_imgs_file.read(1), 'big') > 127) else 1
    
        testing_images.append(new_image)

print('Done reading testing images, now to write...')

if not os.path.exists('testing-images/'):
    os.mkdir('testing-images')

if not os.path.exists('test/'):
    os.mkdir('test')

with open('t10k-labels.idx1-ubyte', 'rb') as test_lbls_file:
    test_lbls_file.read(8)
    for idx, img in enumerate(testing_images):
        test_img_name = 'testing-images/mnist-image-%d.png' % idx
        print('Image #%s' % (idx + 1), end='\r')
        testing_lbls[test_img_name] = int.from_bytes(test_lbls_file.read(1), 'big')
        np.int8(img)
        label_folder = testing_lbls[test_img_name]
        folder_path = 'test/%d/' % label_folder
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        train_img_name = folder_path + '/img-%d.csv' % idx
        np.savetxt(train_img_name, img, delimiter=',', fmt="%1d")
        #Image.fromarray(img).convert('RGB').save(test_img_name)

# with open('testing-labels.json', 'w') as test_lbls_json:
#     json.dump(testing_lbls, test_lbls_json)


print('Done.')
