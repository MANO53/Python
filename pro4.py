import random
choise1=("rock ,paper ,scissors").split(" ,")
coise_computer =random.choice(choise1)
print(coise_computer)
print("welcome to the ('roce, baber, scissores  ') game :")
h=input("press Enter to continue or type (Help) for the rules help :").lower()

if h=="help":
    print("""******RULES******
          1)You chose and the computer 
          2)Rock smashes scissors ->Rock win 
          3)scissors cut paper -> scissors win 
          4)paper covers rock -> paper win """)
    choise=input("Enter the choise (rock , paper ,scissors ) ")
    print(coise_computer)
    if choise=="paper"and coise_computer =="paper":
        print("we are the same ")
    elif choise=="paper"and coise_computer=="rock":
        print(f"sorry! you lose the coise computer {coise_computer}")
    elif choise=="paper"and coise_computer=="scissors":
        print(f"sorry! you lose the coise computer {coise_computer}")
    elif choise=="rock"and coise_computer=="rock":
        print("you same the choise ")
    elif choise=="rock"and coise_computer=="paper":
        print(f"sorry! you lose the choise computer {coise_computer}")
    elif choise=="rock" and coise_computer=="scissors":
        print(f"sorry ! you lost the coise computer {coise_computer} ")
    elif choise=="scissors" and coise_computer=="scissors":
        print("you are same ")
    elif choise =="scissors" and coise_computer=="paper":
        print(" good jop you win ")
    elif choise=="scissors" and coise_computer=="rock":
        print(f"sorry! you lose the coise computer {coise_computer}")
    else:
        print("inveland choise  sorry you must Enter (rock, paper, scissors)")
else:
    choise=input("Enter the choise (rock , paper ,scissors ) ")
    print(coise_computer)
    if choise=="paper"and coise_computer =="paper":
        print("we are the same ")
    elif choise=="paper"and coise_computer=="rock":
        print(f"sorry! you lose the coise computer {coise_computer}")
    elif choise=="paper"and coise_computer=="scissors":
        print(f"sorry! you lose the coise computer {coise_computer}")
    elif choise=="rock"and coise_computer=="rock":
        print("you same the choise ")
    elif choise=="rock"and coise_computer=="paper":
        print(f"sorry! you lose the choise computer {coise_computer}")
    elif choise=="rock" and coise_computer=="scissors":
        print(f"sorry ! you lost the coise computer {coise_computer} ")
    elif choise=="scissors" and coise_computer=="scissors":
        print("you are same ")
    elif choise =="scissors" and coise_computer=="paper":
        print(" good jop you win ")
    elif choise=="scissors" and coise_computer=="rock":
        print(f"sorry! you lose the coise computer {coise_computer}")
    else:
        print("inveland choise  sorry you must Enter (rock, paper, scissors)")
