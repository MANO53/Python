import random 
number=random.randint(1,11)
gess_number=eval(input("guess a number between 1 and 10 : "))
while gess_number!=number:
    if gess_number>number:
        gess_number=eval(input("too high gess again : "))
    else:
        gess_number=eval(input("too low gues again : "))
        
print("congratulation! you guess the number")