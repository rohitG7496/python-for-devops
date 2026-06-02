import sys
import os

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print(output)

    if operation == "sub":
    outputs = sub(num1, num2)
    print(outputs)