
print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ██╗███╗░░██╗  ██╗░░██╗░█████╗░███████╗██████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██║████╗░██║  ██║░██╔╝██╔══██╗██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ██║██╔██╗██║  █████═╝░███████║█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ██║██║╚████║  ██╔═██╗░██╔══██║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██║██║░╚███║  ██║░╚██╗██║░░██║██║░░░░░██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝

███████╗██╗░░░░░░██████╗██╗░░██╗██╗██╗░░██╗██╗░░██╗
██╔════╝██║░░░░░██╔════╝██║░░██║██║██║░██╔╝██║░░██║
█████╗░░██║░░░░░╚█████╗░███████║██║█████═╝░███████║
██╔══╝░░██║░░░░░░╚═══██╗██╔══██║██║██╔═██╗░██╔══██║
███████╗███████╗██████╔╝██║░░██║██║██║░╚██╗██║░░██║
╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝""")
go=input("welcome in kafr elshikh\n where are you go in kafr elshikh: ")
print(f"good you want go {go} ")
ride =input("What do you want to ride a 🚖🚖🚖taxi or a🚍🚍🚍 bus or a🚂🚂🚂 train\n").lower()
if ride=="bus":
    print(f"sorry!you don't have a⏳⏳⏳ nice time to {ride} ")
elif ride=="train":
    print("sorry!You are tired🥱🥱🥱 because of your work")
elif ride=="taxi":
    print(f"good now you want to go {ride}")
    tax=input("you want to chose \n what you want a ride🚘🚘🚘 ubber or 🚖🚖🚖taxi\n").lower()
    if tax=="ubber":
        print(f"sorry !It is not found {tax} in Kafr El-Sheikh")
    elif tax=="taxi":
        print("ok now we need to go ")
        pay=input("how do you want to pay cach or visa\n :  ").lower()
        if pay=="visa":
            print("sory!i don't have Visa machine ")
        elif pay=="cach":
            print("All right, pay 💲💲💲the driver.")
        else:
            print("inveland choise🤷🤷🤷 ")
    else:
        print("inveland choise🤷🤷🤷 ")
else:
    print("inveland choise 🤷🤷🤷")
