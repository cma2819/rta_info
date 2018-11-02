# -*- coding: utf-8 -*-

import sys
import math

if len(sys.argv) < 2:
    print('Cannnot Calcurate with this Argument')
    exit()
try:
    int(sys.argv[1])
except:
    print('Cannot Parse to Integer')
    exit()

deposit = int(sys.argv[1])
MAX_MARGIN = 99999
RATE = 0.005

flg = True

margin = 0
cnt = 0
while flg:
    margin += int(deposit*RATE)
    #deposit = deposit + int(deposit*RATE)
    cnt += 1
    print('[' + str(cnt) + ']' + str(margin) + ' / ' + str(deposit + margin))
    if margin >= MAX_MARGIN:
        flg = False

print('margin reached to max when ' + str(cnt) + ' months after')
year = math.ceil(cnt / 12)
print('It mean you skip ' + str(year) + ' year(s)')
    