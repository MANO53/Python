#بسم الله الرحمن الراحيم ==>
#rock paper scissors 
import random

choise=("rock ,paper ,scissors").split(" ,")
h =random.choice(choise)
print(h)


rock_asccii="👊"
paper_ascci="✋"
scissors_ascii="✌"
print("welcom to tho Rock Paper scissors game :")
j=input("press enter to continue or type (HELP) for rules : ").lower()
if j=="help":
    print("""******RULES******
          1)You chose and the computer 
          2)Rock smashes scissors ->Rock win 
          3)scissors cut paper -> scissors win 
          4)paper covers rock -> paper win """)
f=input("enter your choise rock paper scissors ")
if f not in ["rock", "paper", "scissors"]:
   print("inveland choise please enter rock paper scissors")
else:
 if f =="rock":
        print(f" your choise\n {rock_asccii}")
 elif f=="paper":
        print(f" your choise\n {paper_ascci}")
 else:
        print(f" your choise\n {scissors_ascii}")
if h =="rock":
    print(f" the coise computer\n  {rock_asccii}")
elif h=="paper":
    print(f" the coise computer\n  {paper_ascci}")
else:
    print(f" the coise computer\n  {scissors_ascii}")
if f==h :
    print("It's a tie ")
elif (
    (f=="rock" and h=="scissors")
    or
    (f=="paper" and h=="rock")
    or
    (f=="scissors"and h=="paper")
):
    print(f"you win {f} beats {h} .")
else:
    print(f"you lose {h} beats {f} .")