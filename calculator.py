"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
user_input = raw_input("Please enter operator and numbers: ")
index = user_input.split(" ")
first= int(index[1])
if len(index)==3:
    second = int(index[2])
    
if index[0] == "+":
    print add(first, second)

elif index[0] == "-":
    print subtract(first, second)
elif index[0] == "*":
    print multiply(first, second)
elif index[0] == "/":
    print divide(first, second)
elif index[0] == "square":
    print square(first)
elif index[0] == "cube":
    print cube(first)
elif index[0] == "pow":
    print pow(first, second)
elif index[0] == "mod":
    print mod(first, second)
else:
    print "quit"



