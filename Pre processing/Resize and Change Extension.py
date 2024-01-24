#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:54:18 2023

@author: alisina
"""

# import required modules 
import cv2 as cv
import os

# If you have different PREFIX of file you can change it here.
PREFIX = "/a"

def get_info():
    """
    DOCSTR:: Just getting information from user!
    
    Returns
    -------
    root_dir, file_extension, file_size

    """
    root_dir = input("Enter the root directory: ")
    file_extension = input("Enter the file extension as you want: ")
    file_size = input("Enter the size of image: ")
    source_dir = input("Enter the parent directory to read the images from that: ")
    return (root_dir, file_extension, file_size, source_dir)
    
    
def find_file_name_and_extension(filename):
    """
    
    Parameters
    ----------
    filename : Get the image to find the filename and extension
    for write the image in manual desinatin with different format or extension.

    Returns
    -------
    fname : Just returned for write the image to another location with this name.
        
    fextension : Returned to define the another extension instead of that.
    It means the user understands! what extension does file have?

    """
    fname = ""
    fextension = ""
    
    for exten in [".jpeg", ".jpg", ".png"]:
        # Find the file extension!
        extension = -5 if exten == ".jpeg" else -4
        result = filename.endswith(exten)  
        if result:
            fname = filename[:extension]        # file name
            fextension = exten                  # file extension
    
    return (fname, fextension)

def resize_and_extension(img, size, extension, source = "."):
    """
    Parameters
    ----------
    img : give the image and read it from location, after this operation resize the
    image and change the extension of image(writing image with diff extension!).

    Returns
    -------
    None.

    """
    finfo = find_file_name_and_extension(img[-1])
    path = source + img[1] + img[2]
    image = cv.imread(path)
    image = cv.resize(image, (size, size))
    result = cv.imwrite(img[0] + img[1] + finfo[0] + "." + extension, image)
    # print("Successfuly :) ") if result else print("Failed (: ")
        
def main():
    """
    DOCSTR:: Start Point of program!
    Find the relative or absolute path of image and pass to the 
    Resize_and_extension() functions as a parameters !

    """
    letters = ["ا", "آ", "ب", "پ", "ت","ث", "ج", "ح", "خ", "د","ذ", "ر", "ز", "س", "ش","ص", "ض", "ط", "ظ", "ع","غ", "ف", "ق", "ک","گ","ل", "م", "ن", "ه", "و", "ء", "ی"]
    
    # Get info from user!
    info = get_info()
    try:
        opr = os.mkdir(info[0])
        print("\n\nStarting ...")
        print("Please Waiting, It takes some time ...")
        steps = ("Train", "Test")
        for step in steps:
            number_of_image = 800 if step == "Train" else 200
            os.mkdir(info[0] + "/" + step)
            print(step + " Step >>>>")
            for l in letters:
                os.mkdir(info[0] + "/" + step + "/" + l) # create the directory for operation!
                # Get the filename from folder!
                files = os.listdir(info[-1] + "/" + step + "/" + l)
                # Get the current file extension! (filename, extension)
                temp_file_info = find_file_name_and_extension(info[-1] + "/" + step + "/" + l + "/" + files[0])
                print("Completed the operation of " + l + "!")
                for img in range(1, number_of_image + 1):
                    img_path = (info[0], "/" + step + "/" + l , PREFIX + str(img) + str(temp_file_info[-1]))
                    resize_and_extension(img_path, int(info[2]), str(info[1]), info[-1])
    
    except:
        print("Some errors occured !!!")

        
#resize_and_extension("304.jpeg", 64, "png")

main()

