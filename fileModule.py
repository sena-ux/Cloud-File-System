from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import formInputFile
import os
import subprocess

def show_file_menu(window):
    # Panel Body
    header = Frame(window)
    header.place(x=300, y=60, width=1070, height=820)

    heading = Label(window, text='Management File', font=('', 13, 'bold'), fg='#0064b3', bg='#eff5f6')
    heading.place(x=325, y=70)
    
    # ==== Frame 1 ====
    bodyFrame1 = Frame(window, bg='#ffffff')
    bodyFrame1.place(x=328, y=110, width=925, height=560)
    
    # ============================ HEADER =====================================
    # ========= LINE ==========
    lineSidebar = Label(window, text="____________________________________________________________________________________________________________________________________________________________________________________" , background='#ffffff')
    lineSidebar.place(x=338, y=140)
    
    
    insert_image_open = Image.open('images\\icons8-plus-25.png')
    insert_image_file = ImageTk.PhotoImage(insert_image_open)
    header_insert = Button(window, image=insert_image_file, bg='#ffffff', bd=0, fg='white', command=lambda: form_Input_File('form', window))
    header_insert.image = insert_image_file
    header_insert.place(x=338, y=120)
    
    
    #insert_image_open = Image.open('images\\icons8-search-25.png')
    #insert_image_file = ImageTk.PhotoImage(insert_image_open)
    #header_insert = Button(window, image=insert_image_file, bg='#ffffff', bd=0, fg='white')
    #header_insert.image = insert_image_file
    #header_insert.place(x=370, y=120)
    
    # ========================== END HEADER ===================================
    
    
    # ============================ CONTENT =====================================
    label_content_text = Label(window, text='File System', bg='#ffffff', font=('', 12, ''))
    label_content_text.place(x=338, y=160)
    
    
    # Canvas
    canvas = Canvas(window, bg='#dbdbdb', width=900, height=460)
    canvas.place(x=338, y=190)

    # Scrollbar
    scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollbar.place(x=1224, y=190, height=464)

    # Frame untuk konten
    content_frame = Frame(canvas, bg='#ffffff')
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Fungsi untuk menyesuaikan ukuran canvas saat konten diubah
    def configure_canvas(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=900, height=460)

    content_frame.bind("<Configure>", configure_canvas)

    # ============================== Content ==================================
    # image_content_imagefile_open = Image.open('images\\icons8-file-100.png')
    # image_content_imagefile_file = ImageTk.PhotoImage(image_content_imagefile_open)
    # label_content_images = Label(content_frame, image=image_content_imagefile_file, bg='#dbdbdb')
    # label_content_images.image = image_content_imagefile_file
    # label_content_images.pack()
    directory = 'file\\system'
    show_file_in_directory(directory, content_frame)
    
    # ============================ End Content ================================

    # Hubungkan scrollbar dengan canvas
    canvas.config(yscrollcommand=scrollbar.set)
    
    
    # ========================== END CONTENT ===================================
    
def form_Input_File(form, window):
    if form == "form":
        formInputFile.show_form_input_file(window)
        
def open_file(file_path):
    try:
        subprocess.Popen([file_path], shell=True)
    except Exception as e:
        messagebox.showerror(title='Error', message=f"Error: {e}")
    
def bind_double_click(button, file_path):
    button.bind("<Double-Button-1>", lambda event, path=file_path: open_file(path))
    

def show_file_in_directory(directory, content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Dapatkan daftar file dalam direktori
    files = os.listdir(directory)

    # Tampilkan setiap file sebagai button dan label dalam content_frame
    row_index = 0  # Indeks baris awal
    column_index = 0  # Indeks kolom awal
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):  # Pastikan itu adalah file, bukan direktori
            file_icon_image = Image.open('images\\icons8-file-100 (1).png')
            file_image_file = ImageTk.PhotoImage(file_icon_image)
            button_file_image = Button(content_frame, image=file_image_file, bd=0, activebackground='#ffffff', bg='#ffffff', padx=20, pady=20, )
            button_file_image.image = file_image_file
            button_file_image.grid(row=row_index, column=column_index, padx=10, pady=10, sticky="nsew")

            label = Label(content_frame, text=file_name, bg='#ffffff', wraplength=150)  # Set panjang pembungkus teks sesuai kebutuhan
            label.grid(row=row_index + 1, column=column_index, padx=10, pady=(0, 10), sticky="nsew")

            # Event 2 kali klik
            bind_double_click(button_file_image, file_path)
            
            # Perbarui indeks baris dan kolom
            column_index += 1
            if column_index == 3:  # Jumlah kolom maksimum
                column_index = 0
                row_index += 2  # Loncat dua baris untuk memberikan ruang antara setiap item

            # Tambahkan referensi ke gambar dan teks ke widget
            button_file_image.image = file_image_file
            label.file_name = file_name


