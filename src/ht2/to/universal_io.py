"""
load and save popular file formats that fits most of the use cases,
* no streaming support, load the whole file into memory
* image: everything that opencv supports
* video: 
* text: txt, csv, json, jsonl, yaml
"""

import os        
import cv2        
import json        
import yaml        
import pandas as pd        
        
def uni_load(filepath):        
    """Load a file from a given filepath.        
        
    Args:        
        filepath (str): The path to the file to load.        
        
    Returns:        
        data: The loaded file data.        
    """        
    ext = os.path.splitext(filepath)[1]        
        
    if ext in [".jpg", ".jpeg", ".png", ".bmp"]:        
        data = cv2.imread(filepath)        
    elif ext in [".mp4", ".avi"]:        
        data = cv2.VideoCapture(filepath)        
    elif ext in [".txt"]:        
        with open(filepath, "r") as f:        
            data = f.read()        
    elif ext in [".csv"]:        
        data = pd.read_csv(filepath)        
    elif ext in [".json", ".jsonl"]:        
        with open(filepath, "r") as f:        
            data = json.load(f)        
    elif ext in [".yaml", ".yml"]:        
        with open(filepath, "r") as f:        
            data = yaml.safe_load(f)        
    else:        
        raise ValueError(f"Unsupported file type: {ext}")        
        
    return data        
        
def uni_save(filepath, data):        
    """Save data to a file at a given filepath.        
        
    Args:        
        filepath (str): The path to the file to save.        
        data: The data to save.        
    """        
    ext = os.path.splitext(filepath)[1]        
        
    if ext in [".jpg", ".jpeg", ".png", ".bmp"]:        
        cv2.imwrite(filepath, data)        
    elif ext in [".mp4", ".avi"]:        
        data.release()        
    elif ext in [".txt"]:        
        with open(filepath, "w") as f:        
            f.write(data)        
    elif ext in [".csv"]:        
        data.to_csv(filepath, index=False)        
    elif ext in [".json", ".jsonl"]:        
        with open(filepath, "w") as f:        
            json.dump(data, f)        
    elif ext in [".yaml", ".yml"]:        
        with open(filepath, "w") as f:        
            yaml.dump(data, f)        
    else:        
        raise ValueError(f"Unsupported file type: {ext}")        
        
    
