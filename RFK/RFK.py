import os, random, string, sys
from pathlib import Path
#from . import rfkeygen

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

def GenKey():
    name = input("Please input your name:\n> ")
    alphabet = string.ascii_letters + string.digits
    password = input("\n\nPlease input a password:\n> ")
    seedphrase = ''.join(random.choice(alphabet) for i in range(0,4096))
    seedphrase += password
    GenKeypair(seedphrase, name, password)


def ImportKey():
    print(1)

def EncryptMessage():
    print(1)

def DecryptMessage():
    print(1)


import base64
import json

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
    " " : 2689,
    "!" : 1451,
    "£" : 1123,
    '"' : 317,
    "$" : 613,
    "%" : 1069,
    "^" : 7649,
    "&" : 5281,
    "*" : 2551,
    "(" : 4903,
    ")" : 5519,
    "-" : 4111,
    "_" : 4211,
    "=" : 1877,
    "+" : 5,
    "[" : 4229,
    "]" : 6701,
    ":" : 7717,
    ";" : 4019,
    "'" : 6329,
    "@" : 5879,
    "#" : 2137,
    "~" : 641,
    "," : 5843,
    "<" : 5381,
    "." : 2351,
    "/" : 7727,
    "?" : 7879,
    "`" : 61,
    "¬" : 997,
}

def GenKeypair(seedphrase, name, password):
    ReturnHash = rfh2048(seedphrase)
    total = str(ReturnHash)
    n = len(total)
    if n%2 == 0:
        privatekeyhalf = total[0:n//2]
        publickeyhalf = total[n//2:]
    else:
        privatekeyhalf = total[0:(n//2+1)]
        publickeyhalf = total[(n//2+1):]

    total = rfh2048(password)
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    final = BinToHex(steptwo)
    password = final[:512]

    link = privatekeyhalf + publickeyhalf

    publickey = base64.b85encode(bytes(publickeyhalf, 'utf-8'))
    privatekey = base64.b85encode(bytes(privatekeyhalf, 'utf-8'))

    kr_block = {
        "pubkey" : publickey.decode('utf-8'),
        "privkey" : privatekey.decode('utf-8'),
        "name" : name,
        "password" : password
    }

    jsonkr = json.dumps(kr_block)

    with open("keyring.kr", "a+") as kr:
        kr.write(jsonkr)
        kr.write("\n")
        kr.close()

    encoded_pub = EncodePubKey(publickey, name)
    encoded_priv = EncodePrivKey(privatekey, name, link)

    pubfile = name
    pubfile += ".pub"
    privfile = name
    privfile += ".priv"

    with open(pubfile, "w+") as pubf:
        pubf.write(encoded_pub)
        pubf.close()

    with open(privfile, "w+") as privf:
        privf.write(encoded_priv)
        privf.close()

def EncodePubKey(publickey, name):
    out = ''.join("               ----- BEGIN RF PUBKEY BLOCK -----\n\n\n")
    out += "Name:  " + name + "\n\n"
    count = 0
    publickey = publickey.decode('utf-8')
    for character in publickey:
        count += 1
        if count == 64:
            out += "\n"
            count = 0
        else:
            out += character
    out += "\n               ----- END RF PUBKEY BLOCK -----"
    return out

def EncodePrivKey(privatekey, name, link):
    out = ''.join("              ----- BEGIN RF PRIVKEY BLOCK -----\n\n\n")
    out += "Name:  " + name + "\n"
    out += "Link:  " + link + "\n\n"
    count = 0
    privatekey = privatekey.decode('utf-8')
    for character in privatekey:
        count += 1
        if count == 64:
            out += "\n"
            count = 0
        else:
            out += character
    out += "\n              ----- END RF PRIVKEY BLOCK -----"
    return out

def rfh2048(str_to_hash):
    total = 0
    count = 1
    for letter in str_to_hash:
        total += (StringToNumbers[letter]*count)
        count += 1
    total *= (877653 * 3301 * 1033)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    count = 1
    for letter in stepthree:
        total += (StringToNumbers[letter]*count)
        count += 1
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    count = 1
    for letter in stepthree:
        total += (StringToNumbers[letter]*count)
        count += 1
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    stepthree = BinToHex(steptwo)
    count = 1
    for letter in stepthree:
        total += (StringToNumbers[letter]*count)
        count += 1
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
    n = len(stepthree)
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
    total2 = 0
    for letter in string1:
        total2 += XORFunction(StringToNumbers[letter], 1033)
    for letter in string2:
        total2 += XORFunction(StringToNumbers[letter], 3301)
    for letter in stepthree:
        total += StringToNumbers[letter]
    for i in range(0,512):
        total *= (XORFunction(total, total2)*1033*3301)
    total *= ((877653 * 3301 * 1033)*4096)*4096
    stepone = StrToBin(total)
    steptwo = stepone[2:]
    final = BinToHex(steptwo)
    final = final[:512]
    return total

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
    GenKey()

