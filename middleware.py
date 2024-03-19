import formLoginRegisterModule
import userModule
import dashboardModule

def middleware(self, window):
    data = userModule.display_all_data()
    if data[2] == "isLogin":
        logged_in = True
    else :
        logged_in = False
    
    # Check login status and display appropriate screen
    if not logged_in:
        # Display login or register form
        formLoginRegisterModule.show_form_login_register(self, window)
    else:
        # User is logged in, show dashboard
        dashboardModule.show_dashboard(self, window)

