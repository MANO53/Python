import random
import string

password=[]



pas=eval(input("enter the total number of chracters in the password : "))

# letters     \ numberes      \ symboles    ==> generated .......

letters=eval(input("enter the number of letteres of the password : "))
numberes=eval(input("enetr the number of the numberes in the password: "))
symbols=eval(input("enter the number of the symbols in the password :"))
if pas==letters+numberes+symbols:
    string_litteres=random.choices(string.ascii_letters, k=letters)
    numberes_string=random.choices(string.digits, k=numberes)
    puncetuacion_1=random.choices(string.punctuation, k=symbols)
    password=string_litteres+numberes_string+puncetuacion_1
    random.shuffle(password)
    passcode=" ".join(password)
    print(passcode)
else:
    print("inveland  that's Erorr 404 >>>>>>>>><<<<<<<")