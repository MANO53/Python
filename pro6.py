print("welcome  to multiplicaion table ")
number=eval(input("enter a number "))
print(f" \n multiplication table fo {number} \n ")
for i in range (1,11):
    result=i*number
    print(f"{i} x {number} = {result}")