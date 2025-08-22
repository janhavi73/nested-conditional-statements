medical_cause=(input("please enter whether you have a medical cause: Y or N"))
attend=int(input("please enter your attendance"))

if medical_cause =="Y":
    print("you will be allowed")
else:
    if attend >= 75:
        print("you will be allowed")
    else:
        print("you are not allowed")    

     


