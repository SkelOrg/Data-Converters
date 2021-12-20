from lengthlib import *

type1 = str(input("Enter the name of a length: "))
if type1 in lengthTypes.millimeter:
    length = float(input("Enter length in millimeters: "))
    type2 = str(input("Enter a type of length to convert to: "))

    if type2 in lengthTypes.centimeter:
        length = length / 10
        print(f"Length in centimeters: {length}")
    elif type2 in lengthTypes.meter:
        length = length / 1000
        print(f"Length in meters: {length}")
    elif type2 in lengthTypes.kilometer:
        length = length / 1000 / 1000
        print(f"Length in kilometers: {length}")
    elif type2 in lengthTypes.inch:
        length = length / 25.4
        print(f"Length in inches: {length}")
    else:
        print("Invalid length type")
elif type1 in lengthTypes.centimeter:
    length = float(input("Enter length in centimeters: "))
    type2 = str(input("Enter a type of length to convert to: "))

    if type2 in lengthTypes.millimeter:
        length = length * 10
        print(f"Length in millimeters: {length}")
    elif type2 in lengthTypes.meter:
        length = length / 100
        print(f"Length in meters: {length}")
    elif type2 in lengthTypes.kilometer:
        length = length / 1000 / 100
        print(f"Length in kilometers: {length}")
    elif type2 in lengthTypes.inch:
        length = length / 2.54
        print(f"Length in inches: {length}")
    else:
        print("Invalid length type")
elif type1 in lengthTypes.meter:
    length = float(input("Enter length in meters: "))
    type2 = str(input("Enter a type of length to convert to: "))

    if type2 in lengthTypes.millimeter:
        length = length * 1000
        print(f"Length in millimeters: {length}")
    elif type2 in lengthTypes.centimeter:
        length = length * 100
        print(f"Length in centimeters: {length}")
    elif type2 in lengthTypes.kilometer:
        length = length / 1000
        print(f"Length in kilometers: {length}")
    elif type2 in lengthTypes.inch:
        length = length * 39.37
        print(f"Length in inches: {length}")
    else:
        print("Invalid length type")
elif type1 in lengthTypes.kilometer:
    length = float(input("Enter length in kilometers: "))
    type2 = str(input("Enter a type of length to convert to: "))

    if type2 in lengthTypes.millimeter:
        length = length * 1000 * 1000
        print(f"Length in millimeters: {length}")
    elif type2 in lengthTypes.centimeter:
        length = length * 1000 * 100
        print(f"Length in centimeters: {length}")
    elif type2 in lengthTypes.meter:
        length = length * 1000
        print(f"Length in meters: {length}")
    elif type2 in lengthTypes.inch:
        length = length * 39370.079
        print(f"Length in inches: {length}")
    else:
        print("Invalid length type")
elif type1 in lengthTypes.inch:
    length = float(input("Enter length in inches: "))
    type2 = str(input("Enter a type of length to convert to: "))

    if type2 in lengthTypes.millimeter:
        length = length * 25.4
        print(f"Length in millimeters: {length}")
    elif type2 in lengthTypes.centimeter:
        length = length * 2.54
        print(f"Length in centimeters: {length}")
    elif type2 in lengthTypes.meter:
        length = length / 39.37
        print(f"Length in meters: {length}")
    elif type2 in lengthTypes.kilometer:
        length = length / 39370.079
        print(f"Length in kilometers: {length}")
    else:
        print("Invalid length type")
else:
    print("Invalid length type")