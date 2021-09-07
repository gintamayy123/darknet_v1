import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random




classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

url = '/home/yolo/project/train/src_repo/projects/cfg/yolov4-custom.cfg'              #图片保存的位置根目录



with open(url, 'r') as f:
    print(f.read())



