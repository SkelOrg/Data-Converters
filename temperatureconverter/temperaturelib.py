class temperatureTypes:
    farenheit = ["F", "f"]
    celsius = ["C", "c"]
    kelvin = ["K", "k"]

def farToCel(far):
    cel = (far - 32) * 5 / 9
    return cel

def celToFar(cel):
    far = cel * 9 / 5 + 32
    return far

def kelToFar(kel):
    far = kel * 9 / 5 - 459.67
    return far

def farToKel(far):
    kel = (far + 459.67) * 5 / 9
    return kel

def kelToCel(kel):
    cel = kel - 273.15
    return cel

def celToKel(cel):
    kel = cel + 273.15
    return kel