units=int(input("please enter the amount of units"))

if (units < 50):
    amount=units*2.6
    surcharge=25

elif (units <=100):
    amount= 130+((units-50)*3.25)
    surcharge=35

elif (unit<=200):
    amount=130+162.50+((units-100)*5.26)
    surcharge=45

else:
    amount=130+162.50+526+((units-200)*8.45)
    surcharge=75

total=amount+surcharge
print("\nElectricity bill %.2f" %total )