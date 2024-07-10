corect_password="ash1234"
entered_password=input("enter a password: ")
while entered_password!=corect_password:
    print("incorect password, try again.")
    entered_password=input("enter a password: ")
print("Access granted !")
