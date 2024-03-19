from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time
from tkinter import messagebox
import dashboardModule
import fileModule
import navbar
import sidebar
import os
import formLoginRegisterModule
import userModule
import middleware

        

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('Cloud File System')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        #icon
        #icon = PhotoImage(file='/images/download.ico')
        #self.window.iconphoto(True, icon)
        
        try:
            # Load the icon
            icon = PhotoImage(file='images\\cloud1.png')
        
            # Set the window icon
            self.window.iconphoto(True, icon)
        except Exception as e:
            print("Error:", e)
            
        # =====================================================================
        # ========================= Login =====================================
        # =====================================================================
        
        # Check if user is logged in
        middleware.middleware(self, window)
        
        
    def show_dashboard(self, window):
        
        
        # =====================================================================
        # =========================== BODY ====================================
        # =====================================================================
        
        
        # ========================== DASHBOARD ================================
        
        dashboardModule.show_dashboard(window)
        
        # ======================== END DASHBOARD ==============================
        
        
    def set_login_status(self, status):
        self.logged_in = status
        self.show_dashboard()
        


def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()
    
if __name__ == '__main__':
    win()
    


