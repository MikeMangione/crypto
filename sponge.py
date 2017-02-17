#!/usr/bin/env python

from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

K = "AES w/ fixed key"

def Sponge(input_string, output_len):
    text = []
    init = '0' * len(input_string)
    for x in range(0,len(input_string)/output_len):
        text.append(input_string[x*output_len:(x+1)*output_len])
    temp = strxor(text[0],init[:output_len]) + input_string[output_len:]
    for x in range(0,(len(input_string)/output_len)-1):
        cipher = AES.new(K,AES.MODE_ECB)
        temp = cipher.encrypt(temp)
        temp = strxor(text[x+1],temp[(x+1)*output_len:(x+2)*output_len]) + temp[output_len:]
    out = []
    for x in range(0,(len(input_string)/output_len)):
        out.append(temp[:output_len])
        cipher = AES.new(K,AES.MODE_ECB)
        temp = cipher.encrypt(temp)
    text = ''
    for x in out:
        text += hexlify(x)
    print text

print_command = 'print "CBC-MAC yields a very good hash function"'
Sponge(print_command, 24)
