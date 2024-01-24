#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Wed Nov  2 20:12:48 2022

@author: Ali Sina Nasiri & Mohammad Ali Alizada

"""
import numpy as np
import cv2
import os
import time


def create_folder(fldr):
    """
    fldr: Recieve the folder name. and create it.
          Create the folders for each type of thresholding.
    """
    try:
        os.mkdir(str(fldr))
    except:
        pass
    
def image_to_threshold_binary(img, desination):
    """
    Parameters
    ----------
    img : Read the image from source of target and convert the image to the
          binary type of threshold(Threshold Image Concept).
          it means image will having only two pixels values (0, 1).
          
    desination : Read and Write the image from/into the destination.

    Returns
    -------
        Not Return! But write the image to the desination!
    
    """
    
    
    image = cv2.imread("Data/" + desination + "/" + img)
    thresh, thresh_img = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)
    cv2.imwrite("Binary Threshold Images/" + desination +"/thresh_" + img, thresh_img)
    
def image_to_threshold_binary_inverse(img, desination):
    """
    Parameters
    ----------
    img : Read the image from source of target and convert the image to the
          binary type of threshold(Threshold Image Concept).
          it means image will having only two pixels values (0, 1)

    Returns
    -------
        Not Return! But write the image to the desination!

    """
    
    image = cv2.imread("Data/" + desination + "/" + img)
    thresh, thresh_img = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite("Inverse Binary Threshold Images/" + desination +"/thresh_" + img, thresh_img)
    

def image_to_adaptive_threshold(img, desination):
    """
    Parameters
    ----------
    img : Read the image from source of target and convert the image to the
          binary type of threshold(Threshold Image Concept).
          it means image will having only two pixels values (0, 1)
    destination: Read and Write the image from/into that.
    

    Returns
    -------
        Not Return! But write the image to the desination!

    """
    
    image = cv2.imread("Data/" + desination + "/" + img, 0)
    image_blur = cv2.medianBlur(image, 5)
    image_threshold = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite("Adaptive Threshold Gaussian/" + desination +"/thresh_" + img, image_threshold)

def image_to_adaptive_threshold_mean(img, desination):
    """
    Parameters
    ----------
    img : Read the image from source of target and convert the image to the
          binary type of threshold(Threshold Image Concept).
          it means image will having only two pixels values (0, 1)
    destination: Read and Write the image from/into that.


    Returns
    -------
        Not Return! But write the image to the desination!

    """
    
    image = cv2.imread("Data/" + desination + "/" + img, 0)
    image_blur = cv2.medianBlur(image, 5)
    image_threshold = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite("Adaptive Threshold Mean/" + desination +"/thresh_" + img, image_threshold)

letters = ["ا", "آ", "ب", "پ", "ت","ث", "ج", "ح", "خ", "د","ذ", "ر", "ز", "س", "ش","ص", "ض", "ط", "ظ", "ع","غ", "ف", "ق", "ک","گ","ل", "م", "ن", "ه", "و", "ء", "ی"]


print("""
Menu:
1- [Binary Threshold]
2- [Adaptive Threshold -> GAUSSIAN_C]
3- [Adaptive Threshold -> MEAN]
4- [Inverse Binary Threshold]
""")

menu = int(input("Enter the number of menu(Just Number): "))

for l in letters:
    for img in range(301, 1301):
        if menu == 1:
            create_folder("Binary Threshold Images")
            create_folder("Binary Threshold Images/%s"%(l))
            image_to_threshold_binary(str(img) + ".jpeg", l)
            print("\tThreshold the image #" + str(img) + ".jpeg ...")
        elif menu == 2:
            create_folder("Adaptive Threshold Gaussian")
            create_folder("Adaptive Threshold Gaussian/%s"%(l))
            image_to_adaptive_threshold(str(img) + ".jpeg", l)
            print("\tThreshold the image #" + str(img) + ".jpeg ...")
        elif menu == 3:
            create_folder("Adaptive Threshold Mean")
            create_folder("Adaptive Threshold Mean/%s"%(l))
            image_to_adaptive_threshold_mean(str(img) + ".jpeg", l)
            print("\tThreshold the image #" + str(img) + ".jpeg ...")
        elif menu == 4:
            create_folder("Inverse Binary Threshold Images")
            create_folder("Inverse Binary Threshold Images/%s"%(l))
            image_to_threshold_binary_inverse(str(img) + ".jpeg", l)
            print("\tThreshold the image #" + str(img) + ".jpeg ...")
        else:
            print("You selected a wrong menu ... ")
            
        if img == 1301:
            time.sleep(3000)
            print("\n\nGo to the next directory ...")
            time.sleep(3000)
    