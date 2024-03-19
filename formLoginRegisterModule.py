from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import shutil
import os
from tkinter import ttk
import openpyxl
import userModule

def show_form_login_register(self, window):
    
    # ======= Box =========
    box_frame_form_login_register = Frame(window, bg='#231485', width=2400, height=768)
    box_frame_form_login_register.place(x=0, y=0, width=2400, height=820)
    
    # =========================================================================
    # ========================== REGISTER =====================================
    # =========================================================================
    # Images
    image = Image.open('images\\background.jpg')
    image_file = ImageTk.PhotoImage(image)
    label = Label(window, image=image_file)
    label.image = image_file
    label.place(x=0, y=0)
    
    # TITLE
    label = Label(window, text='Form Login and Register', font=('', 38, ''), fg='#ef1d84', bd=0, highlightthickness=0, bg='#011039')
    label.place(x=350, y=90)

    
    # INPUT 1
    label = Label(window, text='Username ', bg='#ffffff', width=9, font=('', 24, ''), fg='#052e70')
    label.place(x=380, y=220)
    entry_username = Entry(window, width=20, font=('', 24, ''))
    entry_username.place(x=560, y=220)
    
    # INPUT 2
    label = Label(window, text='Password ', bg='#ffffff', width=9, font=('', 24, ''), fg='#052e70')
    label.place(x=380, y=300)
    entry_password = Entry(window, width=20, font=('', 24, ''), show='*')
    entry_password.place(x=560, y=300)
    
    eye_button = Button(window, text="👁️", command=lambda: toggle_password_visibility(entry_username, entry_password), font=('', 16, ''), bd=0, bg='#ffffff')
    eye_button.place(x=855, y=302)


    # BUTTON
    # Membuat ttk.Style untuk tombol
    style = ttk.Style()
    style.configure('TButton', background='#231485', foreground='#ef1d84', font=('', 24), padding=5, borderwidth=0)
    
    # Buat tombol dengan ttk.Button dan gunakan style yang telah dibuat
    button = ttk.Button(window, text='Login', style='TButton', command=lambda: auth("login", entry_username, entry_password, window, self), )

    button.place(x=545, y=390)
    
    data = userModule.display_all_data()
    if not data:
        # BUTTON
        # Membuat ttk.Style untuk tombol
        style = ttk.Style()
        style.configure('TButton', background='#231485', foreground='#ef1d84', font=('', 24), padding=5, borderwidth=0)
        
        # Buat tombol dengan ttk.Button dan gunakan style yang telah dibuat
        button = ttk.Button(window, text='Register', style='TButton', command=lambda: auth("register", entry_username, entry_password, window, self), )
    
        button.place(x=545, y=490)
    
    # =========================================================================
    # ======================= END REGIASTER ===================================
    # =========================================================================


    # =========================================================================
    # ============================ LOGIN ======================================
    # =========================================================================
    
    
    
    # =========================================================================
    # ========================= END LOGIN =====================================
    # =========================================================================
    
    
    
    
def clear(entry_username, entry_password):
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')


def auth(sesi, entry_username, entry_password, window, self):
    try:
        # Mendapatkan nilai dari kotak entri
        username_val = entry_username.get()
        password_val = entry_password.get()
        
        if sesi == "register":
            if username_val == "" and password_val == "":
                messagebox.showerror(title='Error', message='Username and Password not empety!')
                clear(entry_password, entry_username)
            elif len(username_val) <= 5 and len(password_val) <= 8:
                messagebox.showerror(title='Error', message='Username this 5 caracter')
                clear(entry_password, entry_username)
            else :
                userModule.register(username_val, password_val, window, self)
                
        elif sesi == "login":
            if username_val == "" and password_val == "":
                messagebox.showerror(title='Error', message='Username and Password not empety!')
                clear(entry_password, entry_username)
            elif len(username_val) <= 5 and len(password_val) <= 8:
                messagebox.showerror(title='Error', message='Username this 5 caracter')
                clear(entry_password, entry_username)
            else :
                userModule.login(username_val, password_val, window, self)
                
        else:
            print('Invalid session')
    except Exception as e:
        print(f'Error: {e}')


def toggle_password_visibility(entry_username, entry_password):
    current_show_state = entry_password.cget("show")
    if current_show_state == '':
        entry_password.config(show='*')  # Password tersembunyi
    else:
        entry_password.config(show='')   # Password terlihat
        
        
    

