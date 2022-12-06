print("Location: \n1. America \n2. Asia \n3. Africa \n4.Europe\n")
destination = input("Enter your location: ")

print("Time Code: \n[A] Day \n[B] Night")
time = input("Enter time code: ")

print("Day Code: \n[X] Weekdays\n[Y] Weekends")
day = input("Enter Day Code: ")

duration = float(input("Enter call duration: "))

if day == 'X' or day == 'x':
    if time == 'A' or time == 'a':
        if destination == '1':
            charge = duration * (50/3)
        elif destination == '2':
            charge = duration * (30/2)
        elif destination == '3':
            charge = duration * (40/3)
        elif destination == '4':
            charge = duration * (35/2)
        else:
            print("Wrong input ! ! !1")
    elif time == 'B' or time == 'b':
        if destination == '1':
            charge = duration * (45/3)
        elif destination == '2':
            charge = duration * (27/2)
        elif destination == '3':
            charge = duration * (36/3)
        elif destination == '4':
            charge = duration * (30/2)
        else:
            print("Wrong input ! ! !2")
    else:
        print("Wrong input ! ! !3")
elif day == 'Y' or day == 'y':
    if time == 'A' or time == 'a':
        if destination == '1':
            charge = duration * (40/3)
        elif destination == '2':
            charge = duration * (25/2)
        elif destination == '3':
            charge = duration * (35/3)
        elif destination == '4':
            charge = duration * (20/2)
        else:
            print("Wrong input ! ! !4")
    elif time == 'B' or time == 'b':
        if destination == '1':
            charge = duration * (38/3)
        elif destination == '2':
            charge = duration * (15/2)
        elif destination == '3':
            charge = duration * (22/3)
        elif destination == '4':
            charge = duration * (19/2)
        else:
            print("Wrong input ! ! !5")
    else:
        print("Wrong input ! ! !6")
else:
    print("Wrong Input ! ! !7")


print("Total Charge: ", round(charge, 2))