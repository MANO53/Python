import random 
print("""welcome to the coin guessing game !
chose a method to toss the coin : """)
m=eval(input ("""1.using random.randint
2.using random.random 
enter your choise (1 or 2 ): """))
if m==1:
    n=random.randint(0,1)#heads 0         tails 1  
    b=input("enter your guess (heads or tails )").lower() 
    if n==0:
        if b=="heads":
            print("congrateulation ! you win ")
        else :
            print(" sorry! you lost ")
    elif n==1:
        if b=="tails":
            print("congrateulation ! you win ")
        else:
            print("sorry! you lost ")
elif m==2:
    c=random.random()
    b=input("enter your guess (heads or tails )").lower()
    if c>=.5:
        if b=="heads":
            print("congrateulation! you won ")
        else:
            print("sorry! you lost ")
    else:
        if b=="tails" :
            print("congrateulation ! you won ")
        else :
            print("sorry you lost ")
else:
    print("inveland choise , please select 1 or 2 ")