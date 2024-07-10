import random
print("welcome to 'whose wallet ?'")
print("you will give me a list of names , and i wil take a person to pay ")
names=input("if you are ready , enter the names seperated by a comma ....: ").split(" ,")
print(f"please ask {random.choice(names)} to take out his wallet . dinner is on him")