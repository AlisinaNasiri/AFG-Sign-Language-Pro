#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:10:54 2023

@author: alisina & mohammad ali
"""

# required modules
import numpy as np
from random import shuffle
import cv2 as cv
import os

def image_lable(path, bsc_info):
    """
     DOCSTR:: Read the images from directories for labelling and make the train data!

    Returns
    -------
     train_data: Matrix of images!

    """
    
    # Create the txt file for labelling!
    lbl_file = open(str.lower(str(bsc_info)) + "_labels.txt", "w")
    
    train_data = []
    label = 0
    for (dirpaths, dirnames, files) in os.walk(path, topdown= True):
        for directory in dirnames:
            lbl_file.writelines("{ " + str(directory) + " }" + " ----> " + "{ " + str(label) + " }.\n")
            for (dirpaths, dirnames, files) in os.walk(path + "/" + directory, topdown=True):
                for file in files:
                    file_path = path + "/" + directory + "/" + file
                    read_file = cv.imread(file_path, cv.IMREAD_GRAYSCALE)
                    train_data.append([np.array(read_file), label])
            print(label)
            label += 1
    shuffle(train_data)
    np.save(str.lower(str(bsc_info)) + "_data.npy", train_data)
    return train_data


print("""
Just Choose the number of menu(Number):
1- [Convert the train data to numpy array with it's label]
2- [Convert the test data to numpy array with it's label]
""")

def menu():
    """
    Returns
    -------
    src : Is a name of folder that refers to the data and it will return as a source of data.
    
    """
    
    menu_options = int(input("Choose your menu as you want: "))
    src = ""
    if menu_options == 1:
        src = "Train"
    elif menu_options == 2:
        src = "Test"
    else:
        print("You selected the wrong menu, please select the right menu ...")
        src = menu()
        
    return src

rslt = menu()
if rslt:
    source = "Adaptive Threshold Mean Rename/{}/".format(rslt)
    training_data = image_lable(source, rslt)
    print(training_data)
