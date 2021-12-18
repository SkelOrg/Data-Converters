from temperaturelib import *

type1 = str(input("Enter a type of temperature: "))
if type1 in temperatureTypes.celsius:
    temp = float(input("Enter temperature in celsius: "))
    type2 = str(input("Enter a type of temperature to convert to: "))

    if type2 in temperatureTypes.farenheit:
        temp = celToFar(temp)
        print(f"Temperature in farenheit: {temp}")
    elif type2 in temperatureTypes.kelvin:
        temp = celToKel(temp)
        print(f"Temperature in kelvin: {temp}")
    else:
        print("Invalid temperature type")
elif type1 in temperatureTypes.farenheit:
    temp = float(input("Enter temperature in farenheit: "))
    type2 = str(input("Enter a type of temperature to convert to: "))

    if type2 in temperatureTypes.celsius:
        temp = farToCel(temp)
        print(f"Temperature in celsius: {temp}")
    elif type2 in temperatureTypes.kelvin:
        temp = farToKel(temp)
        print(f"Temperature in kelvin: {temp}")
    else:
        print("Invalid temperature type")
elif type1 in temperatureTypes.kelvin:
    temp = float(input("Enter temperature in kelvin: "))
    type2 = str(input("Enter a type of temperature to convert to: "))

    if type2 in temperatureTypes.farenheit:
        temp = kelToFar(temp)
        print(f"Temperature in farenheit: {temp}")
    elif type2 in temperatureTypes.celsius:
        temp = kelToCel(temp)
        print(f"Temperature in celsius: {temp}")
    else:
        print("Invalid temperature type")