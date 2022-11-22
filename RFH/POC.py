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
    for letter in str_to_hash:
        total += StringToNumbers[letter]
    total *= (877653 * 3301 * 1033)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepfour = BinToHex(steptwo)
    n = len(stepfour)
    if n%2 == 0:
        string1 = stepfour[0:n//2]
        string2 = stepfour[n//2:]
    else:
        string1 = stepfour[0:(n//2+1)]
        string2 = stepfour[(n//2+1):]

    stepfive = ''.join(string2)
    stepfive += string1
    for letter in stepthree:
        total += StringToNumbers[letter]
    total *= ((877653 * 3301 * 1033)*4096)*4096
    print(total)
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    final = BinToHex(steptwo)
    final = final[:-4]
    print("Hash: ", final)

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