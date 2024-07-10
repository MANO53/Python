# color=[]
# n=input("add the frist color you like : ")
# color.append(n)
# m=input("do you want to add more  color ? (yes or no )  ").lower()
# if m=="yes":
#     s=input("add another color to the list ")
#     color.append(s)
#     print(f"the color you like are {color}")
# elif m=="no":
#     print(f"the color you like are {color}")
# else:
#     print("inveland choise please enter (yes or no )")

# color2=["white","green","black","yellow"]
# color.extend(color2)
# print(color)
favorite_frutes=["apple","orange","panana"]
guess=input("guess the furites in the basket ")
if guess in favorite_frutes:
    print("good guess ")
else :
    print("sorry! you lost ")