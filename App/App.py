#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:13:05 2023

@author: alisina
"""


# Import Required Libraries
from bidi.algorithm import get_display
import arabic_reshaper
import cv2
import os
import operator
import tkinter as tk
from PIL import Image, ImageTk
from keras.models import model_from_json

os.environ["THEANO_FLAGS"] = "device=cuda, assert_no_cpu_op=True"

# Application parts
class Application:

    def __init__(self):
        self.list_letters = []
        self.word2 = ""
        self.sentence = ""
        self.vs = cv2.VideoCapture(0)
        self.current_image = None
        self.current_image2 = None
        self.json_file = open(r"../Modelling/Models/model_03.json", "r")
        self.model_json = self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.model_json)
        self.loaded_model.load_weights("../Modelling/Models/model_03.h5")
        
        print("Loaded model from disk")

        self.root = tk.Tk()
        self.root.title("AFG Sign Language To Text Conversion")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("700x700")
        self.root.resizable(False,False)

        self.panel = tk.Label(self.root)
        self.panel.place(x = 35, y = 70, width = 625, height = 330)
        
        self.panel2 = tk.Label(self.root) # initialize image panel
        self.panel2.place(x = 400, y = 70, width = 260, height = 230)

        self.T = tk.Label(self.root)
        self.T.place(x = 40, y = 5)
        self.T.config(text = "Sign Language To Text Conversion",border=3,
                      borderwidth=6 ,font = ("Courier", 30, "bold"))

        self.panel3 = tk.Label(self.root) # Current Symbol
        self.panel3.place(x = 300, y = 420)
        self.panel4 = tk.Label(self.root, ) # Word
        self.panel4.place(x = 220,y=460)

        self.T1 = tk.Label(self.root)
        self.T1.place(x = 35, y = 420)
        self.T1.config(text = "Character: ", font = ("Courier", 30, "bold"))
        
        
        self.T = tk.Label(self.root)
        self.T.place(x = 35, y = 480)
        self.T.config(text = "Word: ", font = ("Courier", 30, "bold"))

        self.panel5 = tk.Label(self.root) # Sentence
        self.panel5.place(x = 220, y = 540)

        self.T2 = tk.Label(self.root)
        self.T2.place(x = 35,y = 540)
        self.T2.config(text = "Sentence: ", font = ("Courier", 30, "bold"))
        

        self.bt1 = tk.Button(self.root, text = "Add ",border=1, bg='blue',font=16,
                             borderwidth=2, command = self.add_letter, height = 2, width = 5)
        self.bt1.place(x = 35, y = 620)
        
        self.bt2 = tk.Button(self.root, text = "Space",border=1,bg='pink',font=16,
                             borderwidth=2,command = self.space, height = 2, width = 5)
        self.bt2.place(x = 225, y = 620)
        
        self.b11 = tk.Button(self.root,text = "Delet",border=1,bg='red',font=16,
                             borderwidth=2, command = self.delete_letter, height = 2, width = 6)
        self.b11.place(x = 400, y = 620)
        self.bt3 = tk.Button(self.root,text = "Clear",border=1,bg='red',font=16,
                             borderwidth=2,command = self.clear, height = 2, width = 5,)
        self.bt3.place(x = 580, y = 620)


        self.str = ""
        self.word = " "
        self.current_symbol = ""
        self.video_loop()


    def video_loop(self):
        ok, frame = self.vs.read()
        height,width = frame.shape[: 2]

        if ok:
            cv2image = cv2.flip(frame, 1)

            y1, y2, x1, x2 = 50, 300, 350, 600

            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)

            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image = self.current_image)

            self.panel.imgtk = imgtk
            self.panel.config(image = imgtk)
            
            # Extracting the ROI
            roi = cv2image[y1:y2, x1:x2]

            # Resizing the ROI so it can be fed to the model for prediction
            roi = cv2.resize(roi, (96, 96)) 
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(roi, (7, 7), 2)
            th3 = cv2.adaptiveThreshold(blur, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            
            self.predict(th3)
            
            th3_resized = cv2.resize(th3, (260, 230))
            self.current_image2 = Image.fromarray(th3_resized)

            imgtk = ImageTk.PhotoImage(image = self.current_image2)
            
            self.panel2.imgtk = imgtk
            self.panel2.config(image = imgtk)

            self.panel3.config(text = self.current_symbol, font = ("Courier", 30))

        self.root.after(5, self.video_loop)
    
    def predict(self,test_image):
        test_image = cv2.resize(test_image, (96, 96))
        result = self.loaded_model.predict(test_image.reshape(1, 96, 96, 1))
        
        prediction = {
	        'ا' : result[0][0],
			'آ' : result[0][1],
			'ع' : result[0][2],
			'ب' : result[0][3],
			'د' : result[0][4],
			'ف' : result[0][5],
			'گ' : result[0][6],
			'غ' : result[0][7],
			'ح' : result[0][8],
			'ه' : result[0][9],
			'ء' : result[0][10],
			'ج' : result[0][11],
			'ک' : result[0][12],
			'خ' : result[0][13],
			'ل' : result[0][14],
			'م' : result[0][15],
			'ن' : result[0][16],
			'پ' : result[0][17],
			'ق' : result[0][18],
			'ر' : result[0][19],
			'ث' : result[0][20],
			'ص' : result[0][21],
			'ش' : result[0][22],
			'س' : result[0][23],
			'ت' : result[0][24],
			'ط' : result[0][25],
			'و' : result[0][26],
			'ی' : result[0][27],
			'ذ' : result[0][28],
			'ض' : result[0][29],
			'ز' : result[0][30],
			'ظ' : result[0][31],
        }

        sa = max(result[0]*100)
    
        # Sorting based on top prediction
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)

        if sa>99:
            self.current_symbol = prediction[0][0]
            self.list_letters.append(self.current_symbol)
            self.automatic_word_generator()
            print(prediction[0][0])

    def automatic_word_generator(self):
        if (len(self.list_letters) > 0 and len(self.list_letters) >= 30) and (self.list_letters[len(self.list_letters) - 20::].count(self.list_letters[-1]) == len(self.list_letters[len(self.list_letters) - 20::])):
	        self.add_letter()
	        self.list_letters = []

    def add_letter(self):
        self.word2 = self.word2+self.current_symbol
        self.current_symbol = ""
        self.word3=get_display(arabic_reshaper.reshape(self.word2))
        self.panel4.config(text=self.word3,font=("Courier",40))
        self.panel5.config(text=self.sentence,font=("Courier",40))
        
        
    def space(self):
        self.sentence = self.word3 + " " + self.sentence
        self.word3=""
        self.word2=""
        self.current_symbol = ""
        self.panel4.config(text=self.word3,font=("Courier",40))
        self.panel5.config(text=self.sentence,font=("Courier",40))
        
   
    def delete_letter(self):
        self.current_symbol = ""
        self.word2 = self.word2[:-1]
        self.word3 = self.word3[1:]
        self.panel4.config(text=self.word3,font=("Courier",40))
        
    def clear(self):
        self.current_symbol = ""
        self.word3 = ""
        self.word2= ""
        self.panel4.config(text=self.word3,font=("Courier",40))
        
    def destructor(self):
        print("Closing Application...")
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()
    
print("Starting Application...")
(Application()).root.mainloop()
