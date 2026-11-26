username = "admin"
password = "wrong123"
is_active = True
is_admin = True

if username == "admin" and password == "admin123":
    if is_active and is_admin:
        print("Admin Dashboard")
    elif is_active:
        print("User Dashboard")
    else:
        print("Account Disabled")

else:
    print("Invalid Credentials")