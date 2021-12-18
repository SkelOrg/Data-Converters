from weightlib import *

type1 = str(input("Enter a type of weight: "))
if type1 in weightTypes.pounds:
    weight = float(input("Enter weight in pounds: "))
    type2 = str(input("Enter a type of weight to convert to: "))

    if type2 in weightTypes.kilograms:
        weight = lbsToKg(weight)
        print(f"Weight in kilograms: {weight}")
    elif type2 in weightTypes.stone:
        weight = lbsToSt(weight)
        print(f"Weight in stone: {weight}")
    else:
        print("Invalid weight type")
elif type1 in weightTypes.kilograms:
    weight = float(input("Enter weight in kilograms: "))
    type2 = str(input("Enter a type of weight to convert to: "))

    if type2 in weightTypes.pounds:
        weight = kgToLbs(weight)
        print(f"Weight in pounds: {weight}")
    elif type2 in weightTypes.stone:
        weight = kgToSt(weight)
        print(f"Weight in stone: {weight}")
    else:
        print("Invalid weight type")
elif type1 in weightTypes.stone:
    weight = float(input("Enter weight in stone: "))
    type2 = str(input("Enter a type of weight to convert to: "))

    if type2 in weightTypes.pounds:
        weight = stToLbs(weight)
        print(f"Weight in pounds: {weight}")
    elif type2 in weightTypes.kilograms:
        weight = stToKg(weight)
        print(f"Weight in kilograms: {weight}")
    else:
        print("Invalid weight type")
else:
    print("Invalid input")