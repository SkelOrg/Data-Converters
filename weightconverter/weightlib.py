class weightTypes:
    pounds = ["pounds", "lb", "lbs"]
    kilograms = ["kilograms", "kg", "kilos"]
    stone = ["stone", "st", "stn"]
    ounces = ["ounces", "oz", "ozs"]

def lbsToKg(weight):
    return weight * 0.453592

def lbsToSt(weight):
    return weight * 0.0714286

def kgToLbs(weight):
    return weight * 2.20462

def kgToSt(weight):
    return weight * 0.157473

def stToLbs(weight):
    return weight * 14

def stToKg(weight):
    return weight * 6.35029

def ozToLbs(weight):
    return weight * 0.0625

def ozToKg(weight):
    return weight * 0.02835

def ozToSt(weight):
    return weight * 0.004464

def lbsToOz(weight):
    return weight * 16

def kgToOz(weight):
    return weight * 35.274

def stToOz(weight):
    return weight * 224