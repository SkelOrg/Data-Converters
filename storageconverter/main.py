from storagelib import *

type1 = str(input("Enter a type of storage: "))
if type1 in storageTypes.bit:
    storage = float(input("Enter storage in bits: "))
    type2 = str(input("Enter a type of storage to convert to: "))

    if type2 in storageTypes.byte:
        storage = storage / 8
        print(f"Storage in bytes: {storage}")
    elif type2 in storageTypes.kilobyte:
        storage = storage / 1000
        print(f"Storage in kilobytes: {storage}")
    elif type2 in storageTypes.megabyte:
        storage = storage / 1000 / 1000
        print(f"Storage in megabytes: {storage}")
    elif type2 in storageTypes.gigabyte:
        storage = storage / 1000 / 1000 / 1000
        print(f"Storage in gigabytes: {storage}")
    elif type2 in storageTypes.terabyte:
        storage = storage / 1000 / 1000 / 1000 / 1000
        print(f"Storage in terabytes: {storage}")
    elif type2 in storageTypes.petabyte:
        storage = storage / 1000 / 1000 / 1000 / 1000 / 1000
        print(f"Storage in petabytes: {storage}")
    else:
        print("Invalid storage type")
elif type1 in storageTypes.byte:
    storage = float(input("Enter storage in bytes: "))
    type2 = str(input("Enter a type of storage to convert to: "))

    if type2 in storageTypes.bit:
        storage = storage * 8
        print(f"Storage in bits: {storage}")
    elif type2 in storageTypes.kilobyte:
        storage = storage / 1000
        print(f"Storage in kilobytes: {storage}")
    elif type2 in storageTypes.megabyte:
        storage = storage / 1000 / 1000
        print(f"Storage in megabytes: {storage}")
    elif type2 in storageTypes.gigabyte:
        storage = storage / 1000 / 1000 / 1000
        print(f"Storage in gigabytes: {storage}")
    elif type2 in storageTypes.terabyte:
        storage = storage / 1000 / 1000 / 1000 / 1000
        print(f"Storage in terabytes: {storage}")
    elif type2 in storageTypes.petabyte:
        storage = storage / 1000 / 1000 / 1000 / 1000 / 1000
        print(f"Storage in petabytes: {storage}")
    else:
        print("Invalid storage type")
elif type1 in storageTypes.kilobyte:
    storage = float(input("Enter storage in kilobytes: "))
    type2 = str(input("Enter a type of storage to convert to: "))

    if type2 in storageTypes.bit:
        storage = storage * 1000 * 8
        print(f"Storage in bits: {storage}")
    elif type2 in storageTypes.byte:
        storage = storage * 1000
        print(f"Storage in bytes: {storage}")
    elif type2 in storageTypes.megabyte:
        storage = storage / 1000
        print(f"Storage in megabytes: {storage}")
    elif type2 in storageTypes.gigabyte:
        storage = storage / 1000 / 1000
        print(f"Storage in gigabytes: {storage}")
    elif type2 in storageTypes.terabyte:
        storage = storage / 1000 / 1000 / 1000
        print(f"Storage in terabytes: {storage}")
    elif type2 in storageTypes.petabyte:
        storage = storage / 1000 / 1000 / 1000 / 1000
        print(f"Storage in petabytes: {storage}")
    else:
        print("Invalid storage type")
elif type1 in storageTypes.megabyte:
    storage = float(input("Enter storage in megabytes: "))
    type2 = str(input("Enter a type of storage to convert to: "))

    if type2 in storageTypes.bit:
        storage = storage * 1000 * 1000 * 8
        print(f"Storage in bits: {storage}")
    elif type2 in storageTypes.byte:
        storage = storage * 1000 * 1000
        print(f"Storage in bytes: {storage}")
    elif type2 in storageTypes.kilobyte:
        storage = storage * 1000
        print(f"Storage in kilobytes: {storage}")
    elif type2 in storageTypes.gigabyte:
        storage = storage / 1000
        print(f"Storage in gigabytes: {storage}")
    elif type2 in storageTypes.terabyte:
        storage = storage / 1000 / 1000
        print(f"Storage in terabytes: {storage}")
    elif type2 in storageTypes.petabyte:
        storage = storage / 1000 / 1000 / 1000
        print(f"Storage in petabytes: {storage}")
    else:
        print("Invalid storage type")
elif type1 in storageTypes.gigabyte:
    storage = float(input("Enter storage in gigabytes: "))
    type2 = str(input("Enter a type of storage to convert to: "))

    if type2 in storageTypes.bit:
        storage = storage * 1000 * 1000 * 1000 * 8
        print(f"Storage in bits: {storage}")
    elif type2 in storageTypes.byte:
        storage = storage * 1000 * 1000 * 1000
        print(f"Storage in bytes: {storage}")
    elif type2 in storageTypes.kilobyte:
        storage = storage * 1000 * 1000
        print(f"Storage in kilobytes: {storage}")
    elif type2 in storageTypes.megabyte:
        storage = storage * 1000
        print(f"Storage in megabytes: {storage}")
    elif type2 in storageTypes.terabyte:
        storage = storage / 1000
        print(f"Storage in terabytes: {storage}")
    elif type2 in storageTypes.petabyte:
        storage = storage / 1000 / 1000
        print(f"Storage in petabytes: {storage}")
    else:
        print("Invalid storage type")
elif type1 in storageTypes.terabyte:
    storage = float(input("Enter storage in terabytes: "))
    type2 = str(input("Enter a type of storage to convert to: "))

    if type2 in storageTypes.bit:
        storage = storage * 1000 * 1000 * 1000 * 1000 * 8
        print(f"Storage in bits: {storage}")
    elif type2 in storageTypes.byte:
        storage = storage * 1000 * 1000 * 1000 * 1000
        print(f"Storage in bytes: {storage}")
    elif type2 in storageTypes.kilobyte:
        storage = storage * 1000 * 1000 * 1000
        print(f"Storage in kilobytes: {storage}")
    elif type2 in storageTypes.megabyte:
        storage = storage * 1000 * 1000
        print(f"Storage in megabytes: {storage}")
    elif type2 in storageTypes.gigabyte:
        storage = storage * 1000
        print(f"Storage in gigabytes: {storage}")
    elif type2 in storageTypes.petabyte:
        storage = storage / 1000
        print(f"Storage in petabytes: {storage}")
    else:
        print("Invalid storage type")
elif type1 in storageTypes.petabyte:
    storage = float(input("Enter storage in petabytes: "))
    type2 = str(input("Enter a type of storage to convert to: "))

    if type2 in storageTypes.bit:
        storage = storage * 1000 * 1000 * 1000 * 1000 * 1000 * 8
        print(f"Storage in bits: {storage}")
    elif type2 in storageTypes.byte:
        storage = storage * 1000 * 1000 * 1000 * 1000 * 1000
        print(f"Storage in bytes: {storage}")
    elif type2 in storageTypes.kilobyte:
        storage = storage * 1000 * 1000 * 1000 * 1000
        print(f"Storage in kilobytes: {storage}")
    elif type2 in storageTypes.megabyte:
        storage = storage * 1000 * 1000 * 1000
        print(f"Storage in megabytes: {storage}")
    elif type2 in storageTypes.gigabyte:
        storage = storage * 1000 * 1000
        print(f"Storage in gigabytes: {storage}")
    elif type2 in storageTypes.terabyte:
        storage = storage * 1000
        print(f"Storage in terabytes: {storage}")
    else:
        print("Invalid storage type")
else:
    print("Invalid storage type")