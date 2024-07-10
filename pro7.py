print("**** welcome to ishop calculate *****")
print("let's get to counting them ....")
number=eval(input("how many items are then in your basket today ? "))
pasket=[]
price=[]
for i in range (1,number+1):
    items=input(f"please tell me the name of the item number {i} : ")
    pasket.append(items)
    price_input=eval(input(f"what is the price of {items} \n $ "))
    price.append(price_input)

see=input("would you like to see your inter basket items ? ")
if see =="yes":
    print(pasket)

total_price=input("would you like to see how much it'll cost ? ")
if total_price=="yes":
    print("Buying these itemes will cost",sum(price))

