jop=[]
jop_input=input("enter your task for today seperated by comma : ").split(", ")
jop=jop_input
jop_finish= []
jopnot_finish=[]
for i in jop :
    print(i)
    plan=input(f"did you finish {i} the plant alredy (yes / no)")
    if plan=="yes":
        print("nice jop ")
        jop_finish.append(i)
    else:
        print("i hope to finish it ")
        jopnot_finish.append(i)
        print(jopnot_finish)
    print("---------")
progress=input("do you want to see your today's progress? (yes/no): ")
if progress=="yes":
    print(f"""     *****done tasks *****
          {jop_finish}
                   ***** ongoing tasks *****
          {jopnot_finish} """)
input("press inter to exite ......... ")    
