import sys
sys.path.append('../')
from src import ht2
# TODO revise hyt with label after labeling is done
from glob import glob
from os.path import join,basename
import json
import cv2
from pprint import pprint
from src.ht2.tools.labeling_ops import parse_transcription_label_1

# parse labeled data
label_root = "/data/haotian-test2-pre_anno/"
image_root = "/data/hyt_set/imgs/"
export_root = "/data/hyt_segments/"
all_label_paths = glob(join(label_root,"*.json"))
for label_path in all_label_paths:
    with open(label_path,"r") as f:
        label = json.load(f)
    img_path = join(image_root,label_path.split("/")[-1][:-5]+".jpg")
    # pprint(label)
    img = cv2.imread(img_path)
    cleaned_labels = parse_transcription_label_1(img,label)
    for idx,cleaned_label in enumerate(cleaned_labels):
        cv2.imwrite(join(export_root,"{}_{}.jpg".format(basename(img_path)[:-4],idx)),cleaned_label["img"])
        with open(join(export_root,"{}_{}.txt".format(basename(img_path)[:-4],idx)),"w") as f:
            f.write(cleaned_label["label"])
