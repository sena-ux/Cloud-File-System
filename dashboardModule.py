from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import navbar
import sidebar
import os

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
    
    # Count
    directory = 'file\\system'
    file_count = count_files_in_directory(directory)
    image_count, video_count = count_images_and_videos(directory)
    print(file_count, image_count, video_count)
    
    # Panel Body
    header = Frame(window)
    header.place(x=300, y=60, width=1070, height=820)

    heading = Label(window, text='Dashboard', font=('', 13, 'bold'), fg='#0064b3', bg='#eff5f6')
    heading.place(x=325, y=70)

    # ==== Frame 1 ====
    bodyFrame1 = Frame(window, bg='#ffffff')
    bodyFrame1.place(x=328, y=110, width=925, height=550)

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
    label_frame2_text = Label(window, text=1, font=('', 14, 'bold'), bg='#009aa5')
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
    label_frame2_text = Label(window, text=image_count, font=('', 14, 'bold'), bg='#e21f26')
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
    label_frame2_text = Label(window, text=video_count, font=('', 14, 'bold'), bg='#ffcb1f')
    label_frame2_text.place(x=1120, y=190)
    
    # Text
    label_frame2_title = Label(window, text='Videos dalam aplikasi', font=('', 16, 'bold'), bg='#ffcb1f')
    label_frame2_title.place(x=1000, y=280)
    
    # ============================ End Content ================================
    
    
    
    # ==== Frame 5 ====
    bodyFrame5 = Frame(window, bg='#0aa363')
    bodyFrame5.place(x=348, y=380, width=250, height=220)
    
    # ============================== Content ==================================
    # Images
    image_Frame2_open = Image.open('images\\file_icon.png')
    image_frame_file = ImageTk.PhotoImage(image_Frame2_open)
    labelFrame2 = Label(window, image=image_frame_file, bg='#0aa363', font=('', 14, 'bold'))
    labelFrame2.image = image_frame_file
    labelFrame2.place(x=355, y=388, width=100, height=100)
    
    # Count
    label_frame2_text = Label(window, text=file_count, font=('', 14, 'bold'), bg='#0aa363')
    label_frame2_text.place(x=478, y=430)
    
    # Text
    label_frame2_title = Label(window, text='File lainnya', font=('', 16, 'bold'), bg='#0aa363')
    label_frame2_title.place(x=400, y=520)
    
    # ============================ End Content ================================

def count_files_in_directory(directory):
    try:
        file_count = 0
        for root, dirs, files in os.walk(directory):
            file_count += len(files)
        return file_count
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return 0
    
def count_images_and_videos(directory):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'}
    video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.mpg'}
    
    image_count = 0
    video_count = 0

    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                ext = ext.lower()
                if ext in image_extensions:
                    image_count += 1
                elif ext in video_extensions:
                    video_count += 1
        return image_count, video_count
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return 0, 0
