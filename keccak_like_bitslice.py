#!/usr/bin/env python
import textwrap

def bitsliced_f(input_array):
    output_array_T = [[0 for x in range(0,8)] for x in range(0,12)]
    output_array = ['' for x in range(0,8)]
    for y in range(0,8):
        input_array[y] = textwrap.wrap('0'*(12 - len(bin(input_array[y])[2:])) + bin(input_array[y])[2:],1)
        for x in range(0,12):
            input_array[y][x] = int(input_array[y][x])
    input_T = [[input_array[x][y] for x in range(0,8)] for y in range(0,12)]
    output_array_T[0:3],output_array[3] = input_T[5:8],input_T[4]
    for y in range(0,4):
        output_array_T[4+y] = [(input_T[0+y][x]^(y%2)) for x in range(0,8)]
    for y in range(0,4):
        output_array_T[8+y] = [((input_T[0+y][x]+1%2)&input_T[4+y][x]) ^ input_T[8+y][x] for x in range(0,8)]
    for x in range(0,8):
        temp = '0b'
        for y in range(0,12):
            temp += str(output_array_T[y][x])
        output_array[x] = temp
    return output_array

input_array = [0b000010100001,0b000110110010,0b001011100100,0b001111110111,0b010000101000,0b010100111011,0b011001101101,0b011101111110]
#input_array = [0b000110110010 for x in range(0,8)]#, should output 0b010001011011 for all entries
print bitsliced_f(input_array)
