#!/usr/bin/python3

import sys
num1 = int(sys.argv[1])

if num1 % 3 == 0 and num1 % 7 == 0:
	print("3과 7의 배수")
elif num1 % 3 == 0:
	print("3의 배수") 
elif num1 % 7 == 0:
	print("7의 배수")
else:
	print("-")
