from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import navbar
import sidebar

def show_dashboard(self, window):
    # Clear previous widgets
    for widget in self.window.winfo_children():
        widget.destroy()
    
    # =====================================================================
    # ========================== HEADER ===================================
    # =====================================================================
    
    navbar.show_navbar(self, window)
    
    # =====================================================================
    # ========================= SIDEBAR ===================================
    # =====================================================================
    
    sidebar.show_sidebar(self, window)
    
    
    
    
    # Panel Body
    header = Frame(window)
    header.place(x=300, y=60, width=1070, height=820)

    heading = Label(window, text='Dashboard', font=('', 13, 'bold'), fg='#0064b3', bg='#eff5f6')
    heading.place(x=325, y=70)

    # ==== Frame 1 ====
    bodyFrame1 = Frame(window, bg='#ffffff')
    bodyFrame1.place(x=328, y=110, width=925, height=350)

    # ==== Frame 2 ====
    bodyFrame2 = Frame(window, bg='#009aa5')
    bodyFrame2.place(x=348, y=130, width=250, height=220)
    
    # ============================== Content ==================================
    # Images
    image_Frame2_open = Image.open('images\\group 100x100.png')
    image_frame_file = ImageTk.PhotoImage(image_Frame2_open)
    labelFrame2 = Label(window, image=image_frame_file, bg='#009aa5', font=('', 14, 'bold'))
    labelFrame2.image = image_frame_file
    labelFrame2.place(x=370, y=145, width=100, height=100)
    
    # Count
    label_frame2_text = Label(window, text=1908, font=('', 14, 'bold'), bg='#009aa5')
    label_frame2_text.place(x=490, y=190)
    
    # Text
    label_frame2_title = Label(window, text='Users dalam aplikasi', font=('', 16, 'bold'), bg='#009aa5')
    label_frame2_title.place(x=370, y=280)
    
    # ============================ End Content ================================

    # ==== Frame 3 ====
    bodyFrame3 = Frame(window, bg='#e21f26')
    bodyFrame3.place(x=665, y=130, width=250, height=220)
    
    # ============================== Content ==================================
    # Images
    image_Frame3_open = Image.open('images\\picture 100x100.png')
    image_frame3_file = ImageTk.PhotoImage(image_Frame3_open)
    labelFrame3 = Label(window, image=image_frame3_file, bg='#e21f26', font=('', 14, 'bold'))
    labelFrame3.image = image_frame3_file
    labelFrame3.place(x=690, y=145, width=100, height=100)
    
    # Count
    label_frame2_text = Label(window, text=1908, font=('', 14, 'bold'), bg='#e21f26')
    label_frame2_text.place(x=800, y=190)
    
    # Text
    label_frame2_title = Label(window, text='Images dalam aplikasi', font=('', 16, 'bold'), bg='#e21f26')
    label_frame2_title.place(x=680, y=280)
    
    # ============================ End Content ================================

    # ==== Frame 4 ====
    bodyFrame4 = Frame(window, bg='#ffcb1f')
    bodyFrame4.place(x=980, y=130, width=250, height=220)
    
    # ============================== Content ==================================
    # Images
    image_Frame2_open = Image.open('images\\clapperboard 100x100.png')
    image_frame_file = ImageTk.PhotoImage(image_Frame2_open)
    labelFrame2 = Label(window, image=image_frame_file, bg='#ffcb1f', font=('', 14, 'bold'))
    labelFrame2.image = image_frame_file
    labelFrame2.place(x=1000, y=145, width=100, height=100)
    
    # Count
    label_frame2_text = Label(window, text=1908, font=('', 14, 'bold'), bg='#ffcb1f')
    label_frame2_text.place(x=1120, y=190)
    
    # Text
    label_frame2_title = Label(window, text='Videos dalam aplikasi', font=('', 16, 'bold'), bg='#ffcb1f')
    label_frame2_title.place(x=1000, y=280)
    
    # ============================ End Content ================================
    
    
