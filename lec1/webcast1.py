# helloworld
print("helloworld")

# print statement (string, array, function, class, nested prints)

# none
print(None)

# string
print('This is a "great" course')

# int
print(1)
print(2)
print(1312)
print(0)
print(-12312)

# float
print(1.2123123)

# array
print(["hi", "there", "everybody"])
print([1,2,3,45])

# boolean
print(True)
print(False)

# math operations (+, -, /, *, uneven /, //, %)
print(1+1)
print(1-1)
print(int(1/1))
print(1*1)
print(3/2)
print(3//2)
print(5%2)

# nested prints
print(print(3), print(2))

#functions and pointers/variables
# squares a given number
def square(n):
	return n * n

print(square(5))
print(square(square(5)))
sq = square(17.5)
print(square(sq))

def squareRoot(n):
	return 0

def exponent(n):
	return 0

# prints a given name and returns it for later use
def printAndReturnName(name):
	return None

# for and while loops
# multiplies a and b using a for loop
def multByAddForLoop(a,b):
	result = 0
	for i in range(0,b):
		result += a
	return result

print(multByAddForLoop(5,5))

#ifStatement
def ifEquals(a,b):
	if (a == b or b == a):
		print(a, 'is equal to', b)
	elif (a % b == 0):
		print(a, 'is a multiple of', b)
	else:
		print(a, 'is not equal to and not a multiple of', b)

ifEquals(2,1)

"""
if (True and True) -> True
if (True and False) -> False
if (False and True) -> False
if (False and False) - > False

if (True or True) -> True
if (True or False) -> True
if (False or True) -> True
if (False or False) -> False
"""

# multiplies a and b using a while loop
def multByAddWhileLoop(a,b):
	return 0

# if statements
# determines if the string is 8 letters long
def eightLetterString(string):
	return False

# Examples
# adds items into a shoppingCart array
def addToShoppingCart(item):
	return None

# Print every number from 1-100 except:
# for every multiple of 3 print 'fizz'
# for every multiple of 5 print 'buzz'
# and for every multiple of 3 and 5 print 'fizzbuzz'
def fizzbuzz():
	for i in range(1, 101):
		if (i % 3 == 0 and i % 5 == 0):
			print('fizzbuzz')
		elif (i % 3 == 0):
			print('fizz')
		elif (i % 5 == 0):
			print('buzz')
		else:
			print(i)
	return None

print(fizzbuzz())
