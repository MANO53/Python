import random
print("welcome in geuss game ")
print("chose the method to toss the coin : ")
print("1.using random")
print("2.using randint")
choise=eval(input("enter your choise (1 or 2 )"))
if choise==1:
    if random.random()>=.5:
        computer_coise="heads"
    else:
        computer_coise="tails"
elif choise==2:
    if random.randint(0,1)==0:
        computer_coise="heads"
    else:
        computer_coise="tails"
else:
    print("inveland choise please enter (1 or 2 )")
personal_choise=input("please guess the coin (heads or tails )")
if computer_coise.lower()==personal_choise.lower():
    print("congrateulation ! you win ")
else :
    print("sorry you lost ")

print( "the computer coise toss resulet  ",computer_coise)
