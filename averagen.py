#!/usr/bin/env python3
n = 10
inputnum = []
sum = 0
for x in range(1,11):
	print("Please input the {} number:".format(x))
	inputnum[x-1] = input()
print("Input complete,start calculating:")
for y in range(10):
	sum += inputnum[y]
print("The result is : {}".format(sum))