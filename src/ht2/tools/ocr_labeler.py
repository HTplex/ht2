"""
OCR labeler tool.
"""
from os.path import join,exists,splitext
import os
from glob import glob
import random
from  src.ht2.utils_dev.visualize import show_img_np
import cv2
from tqdm import tqdm


class OCRLabeler:
    def __init__(self,image_root,tag="_label",shuffle=False):
        """init and scan all images in image_root

        Args:
            image_root (_type_): root of images
            tag (str, optional): tag to append to label file. Defaults to "_label".
        """
        self.image_root = image_root
        img_exts = ["jpg","jpeg","png"]
        self.images_paths = []
        self.tag = tag
        for ext in img_exts:
            self.images_paths += glob(join(image_root,"*."+ext))
        print("total {} images".format(len(self.images_paths)))
        # filter out images that have labels
        self.images_paths = [p for p in self.images_paths if not exists(splitext(p)[0]+tag+".txt")]
        self.images_paths.sort()

        # shuffle
        if shuffle:
            random.shuffle(self.images_paths)
        # sort
        print("{} images left".format(len(self.images_paths)))


    def load_same_path_psudo_label(img_path,exts=[""]):
        """load psudo label from same path

        Args:
            img_path (_type_): _description_

        Returns:
            _type_: _description_
        """
        psudo_labels = []
        for ext in exts:
            psudo_label_path = splitext(img_path)[0]+ext+".txt"
            if exists(psudo_label_path):
                with open(psudo_label_path) as f:
                    psudo_label = f.read()
            else:
                psudo_label = ""
            psudo_labels.append(psudo_label)
        return psudo_labels
    
    

    def label_session(self,exts,psudo_label_loader = load_same_path_psudo_label):
        """label images
        """
        for i,p in tqdm(enumerate(self.images_paths)):
            print("image {} of {}".format(i,len(self.images_paths)))
            print("path: {}".format(p))
            psudo_labels = psudo_label_loader(p,exts)
            show_img_np(cv2.imread(p))
            for idx,psudo_label in enumerate(psudo_labels):
                print("[plabel {}] {}".format(idx,psudo_label))
            all_same = False
            # check if all psudo labels are the same
            if len(set(psudo_labels)) == 1:
                all_same = True
            print("[plabel matchs] ",all_same)

            psudo_label = psudo_labels[0]
            # edit psudolabel 
            label = input("label: ")
            if label == "":
                label = psudo_label
            if label == "!!":
                label = "[invalid]"
            
            # save label
            save_path = splitext(p)[0]+self.tag+".txt"
            with open(save_path,"w") as f:
                f.write(label)
            print("[final label] {}".format(label))
            print("[saved path] {}".format(save_path))


