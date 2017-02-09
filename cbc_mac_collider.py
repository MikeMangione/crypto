#!/usr/bin/env python
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from random import choice
from string import ascii_lowercase

def cbcmac(K, M):
    print len(M)
    assert(len(K)) == 16
    assert(len(M)) == 48
    # <Question 2 response goes here: complete this function!>
    temp = "0000000000000000"
    a = strxor(temp,M[:16])
    #list of cipher results for the next problem
    c = []
    for i in range(0,3):
        cipher = AES.new(K,AES.MODE_CBC,temp)
        temp = cipher.encrypt(a)
        c.append(hexlify(temp))
        if i < 2:
            a = M[(i+1)*16:(i+2)*16]
    print(c)
    return temp

def collide_cbc_mac():
    temp = ""
    M_prime = ['print "CBC-MAC n','']
    k = 0
    while (not all(ord(char) < 127 and ord(char) > 32 and ord(char) != 39 for char in temp)) or len(temp) != 16:
        original_temp = temp
        j = ''.join(choice(ascii_lowercase) for i in range(0,6))
        M_prime[1] = 'ot a hash"'+j
        K = "sixteen byte key"
        temp = "0000000000000000"
        M_prime[0] = strxor(temp,M_prime[0][:16])
        for i in range(0,2):
            cipher = AES.new(K,AES.MODE_CBC,temp)
            temp = cipher.encrypt(M_prime[i][:16])
        temp = int("0x"+hexlify(temp),16)
        temp = hex(temp ^ 0x6171ab8b6fceafe78997b46cb96b84b1)
        modified = False
        if temp[len(temp)-1] == "L":
            temp = temp.lstrip("0x").rstrip("L")
        if len(temp) % 2 != 1:
            temp = temp.decode('hex')
        else:
            temp = original_temp
        k += 1
        if k % 100000 == 0:
            print(k,)

    print('print "CBC-MAC n'+M_prime[1]+temp)

def hash_from_cbcmac(M):
    K = "sixteen byte key"
    return cbcmac(K, M)

print(hex(0x0551c3ea1ca68f81fcf9d718d004ea93 ^ 0x6420686173682066756e6374696f6e22) == '6171ab8b6fceafe78997b46cb96b84b1')
print(hash_from_cbcmac('print "CBC-MAC not a hash"mvskwqe!l][#{OQNR?U:*I') == hash_from_cbcmac('print "CBC-MAC yields a very good hash function"'))

collide_cbc_mac()
