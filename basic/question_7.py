username = "wrong_user"
password = "python123"
is_active = True 

"""
Your requirements:
1. First check whether the username is "admin".
2. If the username is correct, check whether the password is "python123".
3. If both are correct, check whether the account is active.
4. If everything is correct, print "Login successful".
5. If the username is incorrect, print "Invalid username".
6. If the password is incorrect, print "Invalid password".
7. If the account is inactive, print "Account is disabled".
"""

if username == "admin":
    print("username is correct")
    if password == "python123":
        print("Password is correcord")
        if is_active:
            print("Successful login")
        else:
            print("Account is disable")
    else:
        print("Invalid password")

else:
    print("Invalid username")   


