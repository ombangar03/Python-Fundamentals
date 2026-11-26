age = 22
has_license = False
has_permission = True

if not age < 18 and (has_license or has_permission):
    print("Allowed")
else:
    print("Not allowed")