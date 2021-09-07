import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random


sets = ['train','val']

classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

url = '/home/yolo/project/voc'                                                    #图片保存的位置根目录


data_name = 'custom-data'

if  not os.path.exists(join(url,'labels')):
	os.mkdir(join(url,'labels'))

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(url, image_id):
    in_file = open('%s/%s/%s.xml'%(url, data_name,image_id))
    out_file = open('%s/labels/%s.txt'%(url, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')





img_url = join(url,data_name)
files = os.listdir(img_url)
output_file = list()
train_file = list()
test_file = list()
train_pre = 0.8
for file in files:
    if file.split('.')[1] == 'xml' and os.path.isfile(join(img_url,file.split('.')[0] + '.jpg')):
        filename = file.split('.')[0]
        in_file = open(join(img_url,file))
        tree=ET.parse(in_file)
        root = tree.getroot()
        obj_count = 0
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls in classes:
                obj_count += 1
        if obj_count > 0:
            output_file.append(filename)


file_nums = len(output_file)
train_num = int(file_nums * train_pre)

train_file = random.sample(output_file,train_num)
out_set = set(output_file)
train_set = set(train_file)

test_set = out_set-train_set

test_file = list(test_set)


for img_set in sets:

    list_file = open(join(url,img_set+'.txt'),'w')

    if img_set == 'train':
        for img_id in train_file:
            list_file.write('%s/%s.jpg\n'%(img_url,img_id))
            convert_annotation(url,img_id)
        list_file.close()
    else:
        for img_id in test_file:
            list_file.write('%s/%s.jpg\n'%(img_url,img_id))
            convert_annotation(url,img_id)
        list_file.close()

print("generate label is finished\n")








