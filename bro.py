#🐇        🌲
print("welcome to place the rabbit ")
place=[["🌲","🌲","🌲"],["🌲","🌲","🌲"],["🌲","🌲","🌲"]]
print(f"{place[0]}\n{place[1]}\n{place[2]}")
print("where should the rabbit go : ")
way=input("please chouse the row and column : ")
row=int(way[0])
column=int(way[1])
place[row-1][column-1]="🐇"
print("sucsess......")

print(f"{place[0]}\n{place[1]}\n{place[2]}")