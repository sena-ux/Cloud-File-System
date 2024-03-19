# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
import userModule


def show_navbar(self, window):
    header = Frame(window, bg='#009df4')
    header.place(x=300, y=0, width=1070, height=60)
    
    logout_text = Button(window, text='Logout', bg='#32cf8e', font=('', 13, 'bold'), bd=0, fg='white', cursor='hand1', activebackground='red', command=lambda: userModule.logout(self, window))
    #logout_text.place(x=950, y=15)
    logout_text.place(x=1160, y=15)

