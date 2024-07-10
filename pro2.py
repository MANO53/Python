import random 
print("welcome to 'whoso wallet?'")
friendes_names=input("you will give me a ;list of names , and i will pick a person to pay if you are ready , enter the names separated by comaa ... : ")
names =friendes_names.split(" ,")
num=len(names)-1
num2=random.randint(0,num)
print(f"please ask {names[num2]} to take his wallet out . dinner is on him  ")
