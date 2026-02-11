def admin_only(func):
    def wrapper(user):
        if user=="admin":
            func(user)
        else:
            print("invalid user")
    return wrapper
            

@admin_only
def dashboard(user):    
    print("Welcome to the dashboard page")

@admin_only
def listing():
    print("Welcome to the listing page")

@admin_only
def profile():
    print("Welcome to the profile page")

@admin_only
def settings():
    print("Welcome to the settings page")

user="admin"
dashboard(user)
