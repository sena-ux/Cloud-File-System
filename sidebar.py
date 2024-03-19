# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time
import dashboardModule
import fileModule
import navbar
import sidebar


def show_sidebar(self, window):
    sidebar = Frame(window, bg='#ffffff')
    sidebar.place(x=0, y=0, width=300, height=750)
    
    # Date Time
    date_label = Label(window, bg='#ffffff', font=('', 20, 'bold'), width=17)
    date_label.place(x=0, y=10)
    
    time_label = Label(window, bg='#ffffff', font=('', 20, 'bold'), width=17)
    time_label.place(x=0, y=40)
    
    # Start updating date and time
    update_datetime(date_label, time_label, window)
    
    #logo foto
    try:
        logoImage = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(logoImage)
        logo = Label(window, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=70, y=80)
        
    except Exception as e:
        print("Error:", e)
    
    
    # Name of person
    brand = Label(sidebar, text='Cloud File System', bg='#ffffff', font=('', 15, 'bold'))
    brand.place(x=60, y=200)
    
    # garis line
    lineSidebar = Label(sidebar, text="_______________________________________________________" , background='#ffffff')
    lineSidebar.place(x=10, y=230)
    
    
    # MENU 1 
    iconDashboard = Image.open('images\\dashboard1.png')
    icon1 = ImageTk.PhotoImage(iconDashboard)
    iconDashboard1 = Button(window, image=icon1, bg='#ffffff', command=lambda: show_page('dashboard', window), cursor='hand2', bd=0)
    iconDashboard1.image = icon1
    iconDashboard1.place(x=40, y=260)
    
    # button
    labelDashboard = Button(window, text='Dashboard', bg='#ffffff', font=('', 13, 'bold'), bd=0, fg='black', width=15, cursor='hand2', command=lambda: show_page('dashboard', window))
    labelDashboard.place(x=80, y=260)
    
    
    # line menu 1
    # lineSidebar = Label(sidebar, text="_______________________________________________________" , background='#ffffff')
    # lineSidebar.place(x=10, y=280)
    
    
    # MENU 2 
    iconFile = Image.open('images\\file1.png')
    iconFile1 = ImageTk.PhotoImage(iconFile)
    iconFile = Button(window, image=iconFile1, bg='#ffffff', command=lambda: show_page('file', window), cursor='hand2', bd=0)
    iconFile.image = iconFile1
    iconFile.place(x=40, y=300)
    
    # Label
    labelDashboard = Button(window, text='File', font=('', 13, 'bold'), bg='#ffffff',bd=0, cursor='hand2', width=15, justify='left', command=lambda: show_page('file', window))
    labelDashboard.place(x=80, y=300)
    
    
def show_page(page, window):
    if page == 'dashboard':
        dashboardModule.show_dashboard(window)
    elif page == 'file':
        fileModule.show_file_menu(window)

def update_datetime(date_label, time_label, window):
    # Tampilkan date and time
    date_now = time.strftime('%d/%m/%Y')
    time_now = time.strftime('%H:%M:%S')
    
    # Update label
    date_label.config(text=date_now)
    time_label.config(text=time_now)
    
    # Akan berubah setiap 1 detik
    window.after(1000, lambda: update_datetime(date_label, time_label, window))
    
