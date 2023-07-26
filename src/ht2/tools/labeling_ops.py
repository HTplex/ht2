from glob import glob
from os.path import join
import json
from pprint import pprint
import cv2
import numpy as np
import re
from src.ht2.utils_dev.converts import points_to_cnt
from src.ht2.utils_dev.text import clean_up_english_spaces

def cut_segments_from_img(img,cnts):
    """cut segments from image

    Args:
        img (np.array): image
        cnts (list): list of cnts
    Returns:
        list: list of segment images
    """
    segment_imgs = []
    for cnt in cnts:
        mask = np.zeros_like(img)
        cv2.drawContours(mask,[cnt],0,(255,255,255),-1)

        bbox = cv2.boundingRect(cnt)
        segment_img = img[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2]]
        mask = mask[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2]]
        background_color = np.median(segment_img[mask == 0])
        if np.isnan(background_color):
            background_color = 255
        segment_img = np.maximum(255-mask,segment_img)
        segment_img = np.minimum(np.array(np.ones_like(segment_img)*background_color,dtype=np.uint8),segment_img)
        segment_imgs.append(segment_img)
    return segment_imgs


def clean_latex_eng_label(label):
    """remove \\quad
       make sure only one space between words
       make sure only one space after punctuations
       make sure no space before punctuations
       \\insert{xxx} -> xxx

    Args:
        label (_type_): _description_
    """
    label = label.replace("\\quad"," ")
    label = label.replace("\\deletion"," ")
    label = label.replace("\\del"," ")
    label = label.replace("\\insert{"," ")
    label = label.replace("}"," ")

    

    label = clean_up_english_spaces(label)
    return label

def parse_transcription_label_1(img,label):
    """parse label json from labeling platfrom into list of dicts
       of cleaned ones

    Args:
        label (dict): _description_
    Returns:
        list: [{"img":segment_imgs, "text":egment_labels}]
    """
    segment_labels = [] # {"cnt","text"}
    h,w = img.shape[:2]
    for segment in label["result"]["data"]:
        cnt = points_to_cnt(segment["points"],h,w)
        text = segment["text"]
        segment_labels.append({"cnt":cnt,"text":text})
    segment_imgs = cut_segments_from_img(img,[x["cnt"] for x in segment_labels])
    return [{"img":segment_imgs[i],
             "text":clean_latex_eng_label(segment_labels[i]["text"])} for i in range(len(segment_labels))]
        




    

