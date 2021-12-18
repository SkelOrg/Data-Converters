class weightTypes:
    pounds = ["pounds", "lb", "lbs"]
    kilograms = ["kilograms", "kg", "kilos"]
    stone = ["stone", "st", "stn"]

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