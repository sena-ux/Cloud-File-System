from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import shutil
import os

def show_form_input_file(window):
    
    # ======= Box =========
    box_frame_form_input = Frame(window, bg='#32cf8e', width=910, height=470, border=2)
    box_frame_form_input.place(x=338, y=190)
    
    # ====== Input ========
    # Create labels and entry fields for each input
    # file_label = Label(window, text="Select File:", width=10, bg='#32cf8e')
    # file_label.grid(row=0, column=0, padx=(360, 10), pady=230)
    # file_entry = Entry(window, width=40)
    # file_entry.grid(row=0, column=1, padx=(0, 10), pady=230)
    # file_button = Button(window, text="Browse", command=select_file)
    # file_button.grid(row=0, column=2, padx=(10, 20), pady=230)

    file_button_image_open = Image.open('images\\down-arrow.png')
    file_button_image_file = ImageTk.PhotoImage(file_button_image_open)
    file_button_image = Button(window, image=file_button_image_file, bg='#32cf8e', bd=0, activebackground='#32cf8e', command=lambda: select_file())
    file_button_image.image = file_button_image_file
    file_button_image.grid(row=0, column=2, padx=(670, 20), pady=230)
    
    # ======= Label =======
    form_input1_file_label1 = Label(window, text='Choose a File', bg='#32cf8e', font=('', 18, 'bold'))
    form_input1_file_label1.place(x=338, y=520, width=910)
    
    
# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        directory = 'file\\system'
        comfirm = messagebox.askyesnocancel(title='File Selected', message=f"You have selected: {file_path}")
        if comfirm:
            try:
                file_name = os.path.basename(file_path)
                shutil.copy(file_path, directory)
                messagebox.showinfo(title='Success', message=f'File successfully copied to {directory} with file name {file_name}')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy file: {str(e)}")
        else :
            messagebox.showerror(title='Error', message='Tidak Berhasil')
            select_file()

    
    
