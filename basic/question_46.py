email = "  OM.BANGAR@GMAIL.COM  "

email = email.strip().lower()

if email.endswith("@gmail.com"):
    print("Valid Gmail address.")

else:
    print("Invalid Gmail address.")