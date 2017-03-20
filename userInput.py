import sys
import os

s = sys.argv[1]
def calc(pats):
	try:
		lol1 = int(pats)
		print("It's a int")
		return lol1
	except ValueError:
		try:
			lol1 = float(pats)
			print("It's a float")
			print("Use only a integer")
			return lol1
		except ValueError:
			print("It's a string")
			print("Use only a integer")


user_input = raw_input("Number:")
num1 = calc(user_input)
user_input2 = raw_input("Number2:")
num2 = calc(user_input2)

if sys.argv[1] == "add":
	a = num1 + num2
	print(a)
	done = raw_input("Press Enter to quit")
elif sys.argv[1] == "multiply":
	a = num1 * num2
	print(a)
	done = raw_input("Press Enter to quit")
else:
	sys.exit("Go home")