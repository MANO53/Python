names=[]
name=input("enter the first and last name of your friends seperated by a comma :")
names.append(name)
s=" ".join(names)
d=s.split(", ")
print(d)
print(names)
for x in d :
    m=x.split(" ")
    print("--------")
    print(m)
    print("------------")
    print("Abbreviated names : ")
    print(f"{m[0][0]}.{[1][0]}")
    