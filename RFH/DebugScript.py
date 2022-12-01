StringToNumbers = {
    "a" : 1931,
    "b" : 2381,
    "c" : 3301,
    "d" : 6091,
    "e" : 7817,
    "f" : 7103,
    "g" : 457,
    "h" : 2207,
    "i" : 2729,
    "j" : 743,
    "k" : 107,
    "l" : 1229,
    "m" : 29,
    "n" : 4007,
    "o" : 1193,
    "p" : 673,
    "q" : 71,
    "r" : 3889,
    "s" : 1613, 
    "t" : 1721,
    "u" : 1447,
    "v" : 3571,
    "w" : 547,
    "x" : 157,
    "y" : 3203,
    "z" : 2311,
    "A" : 7919,
    "B" : 4759,
    "C" : 3251,
    "D" : 6679,
    "E" : 811,
    "F" : 1783,
    "G" : 11,
    "H" : 631,
    "I" : 4007,
    "J" : 6689,
    "K" : 7829,
    "L" : 2243,
    "M" : 701,
    "N" : 1061,
    "O" : 283,
    "P" : 401,
    "Q" : 607,
    "R" : 113,
    "S" : 5023,
    "T" : 3581, 
    "U" : 7121,
    "V" : 7129,
    "W" : 5009,
    "X" : 6421,
    "Y" : 3253,
    "Z" : 947,
    "1" : 2069,
    "2" : 1409,
    "3" : 3557,
    "4" : 2347,
    "5" : 5113,
    "6" : 4909,
    "7" : 809,
    "8" : 2017,
    "9" : 193,
    "0" : 1033,
}

def Main(str_to_hash):
    total = 0
    count = 1
    for letter in str_to_hash:
        total += (StringToNumbers[letter]*count)
        count += 1
    total *= (877653 * 3301 * 1033)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    print("\nFirst ittr numeric value: ", total)
    print("First ittr bin value: ", steptwo)
    print("First ittr hash: ", stepthree)
    count = 1
    for letter in stepthree:
        total += (StringToNumbers[letter]*count)
        count += 1
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    print("\nSecond ittr numeric value: ", total)
    print("Second ittr bin value: ", steptwo)
    print("Second ittr hash: ", stepthree)
    count = 1
    for letter in stepthree:
        total += (StringToNumbers[letter]*count)
        count += 1
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    print("\nThird ittr numeric value: ", total)
    print("Third ittr bin value: ", steptwo)
    print("Third ittr hash: ", stepthree)
    count = 1
    for letter in stepthree:
        total += (StringToNumbers[letter]*count)
        count += 1
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    print("\nFourth ittr numeric value: ", total)
    print("Fourth ittr bin value: ", steptwo)
    print("Fourth ittr hash: ", stepthree)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    print("\nFifth ittr numeric value: ", total)
    print("Fifth ittr bin value: ", steptwo)
    print("Fifth ittr hash: ", stepthree)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    print("\nSixth ittr numeric value: ", total)
    print("Sixth ittr bin value: ", steptwo)
    print("Sixth ittr hash: ", stepthree)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    print("\nSeventh ittr numeric value: ", total)
    print("Seventh ittr bin value: ", steptwo)
    print("Seventh ittr hash: ", stepthree)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepfour = BinToHex(steptwo)
    print("\nEighth ittr numeric value: ", total)
    print("Eighth ittr bin value: ", steptwo)
    print("Eighth ittr hash: ", stepfour)
    n = len(stepfour)
    if n%2 == 0:
        string1 = stepfour[0:n//2]
        string2 = stepfour[n//2:]
    else:
        string1 = stepfour[0:(n//2+1)]
        string2 = stepfour[(n//2+1):]
    stepfive = ''.join(string2)
    stepfive += string1
    total2 = 0
    for letter in string1:
        total2 += XORFunction(StringToNumbers[letter], 1033)
    for letter in string2:
        total2 += XORFunction(StringToNumbers[letter], 3301)
    total += (total2)-(1033*3301)
    for letter in stepthree:
        total += StringToNumbers[letter]
    for i in range(0,2048):
        total *= XORFunction(total, total2)
    total *= ((877653 * 3301 * 1033)*4096)*4096
    print(total)
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    final = BinToHex(steptwo)
    final = final[:2048]
    print("\nFinal ittr numeric value: ", total)
    print("Final ittr bin value: ", steptwo)
    print("\n\nFINAL HASH: ", final)

def XORFunction(x, y):
    #Initializing resultant variable
    res = 0
  
    # Assuming provided integers are 32 bit integers
    for i in range(31, -1, -1):
          
        # Find the bits of the provided integers
        b1 = x & (1 << i)
        b2 = y & (1 << i)
        b1 = min(b1, 1)
        b2 = min(b2, 1)
  
        # Checks if both integers are either 1s or 0s
        # if not proceeds to peform standard OR operation
        xorBit = 0
        if (b1 & b2):
            xorBit = 0
        else:
            xorBit = (b1 | b2)
  
        # Update the resultant variable
        res <<= 1
        res |= xorBit
    return res

def BinToHex(steptwo):
    value = ''.join([str(x) for x in steptwo])
    binaries = []
    for d in range(0, len(value), 4):
        binaries.append('0b' + value[d:d+4])
    hexes = ''
    for b in binaries:
        hexes += hex(int(b ,2))[2:]
    return hexes    

def StrToBin(str):
    return bin(str)

if __name__ == '__main__':
    strin = input("Input string to hash:\n> ")
    str_to_hash = strin.strip(" ")
    Main(str_to_hash)