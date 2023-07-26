from os.path import join, exists
from glob import glob
import cv2
import random
from time import time
from tqdm import tqdm
import sys
sys.path.append('../')
from src import ht2
import random


def img_aug_worker(img_root):
    print(img_root)
    img_paths = glob(join(img_root,"*.jpg"))
        
    # print(img_paths[0])
    for img_path in img_paths[:]:
        if exists(img_path[:-4]+"_aug.jpg"):
            continue
        if "aug" in img_path:
            continue
        if random.random() > 0.2:
            continue
        img = cv2.imread(img_path)
        h,w = img.shape[:2]
        img = cv2.resize(img,(int(w/h*64),64))
        h,w = img.shape[:2]
        # ht2.show_img_np(img)
        try:
            img_a = ht2.random_augment_textlines(img)
        except:
            img_a = img
        cv2.imwrite(img_path[:-4]+"_aug.jpg", img_a, [int(cv2.IMWRITE_JPEG_QUALITY), 80])


all_data = glob(join("/data/parseq3/parseq_dataset/*"))[:]
print(len(all_data))

from p_tqdm import p_umap

_ = p_umap(img_aug_worker, all_data)
    

