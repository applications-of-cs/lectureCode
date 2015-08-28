# print statement
print("Something")
print([1,2,3])
print(max);
print(range);
print(print(1), print(2))

# data types w/ some omissions (tuples, sets, etc.)
# Applciations: http://zetcode.com/lang/python/datatypes/
print("Integer:", 5)
print("Floating Point Number:", 5.5)
print("Boolean:", True, False)
print("Character:", 'h')
print("String:", "hello")
print("List:", [1,2,3,4,5])
print("Dictionary:", { 'Name': 'Bob', 'email': 'bob@bob.com', 'phone': '111-111-1111' })

# math operations
print("2+2=", 2+2)
print("2-2=", 2-2)
print("2/2=", 2/2)
print("2*2=", 2*2)
print("3/2=", 3/2)
print("3//2=", 3//2)

# functions
def square(a):
	return a*a

print("square(2) = ", square(2))

def getAndPrintName(name):
	print(name)
	return name

# instance variables
def variables():
	v1 = 1
	v2 = "str"
	v3 = max
	v4 = [1,2,3]
	v5 = 1.2
	return [v1,v2,v3,v4,v5]
print('[v1,v2,v3,v4,v5] =', variables())

myname = getAndPrintName("felix")
print("my name:", myname)

# for and while loops
def multByAddForLoop(a,b):
	result = 0
	for i in range(0, b):
		result += a
	return result

print("multByAddForLoop(3,2) = ", multByAddForLoop(3,2))

def multByAddWhileLoop(a,b):
	result = 0
	while(b > 0):
		result += a
		b -= 1
	return result
print("multByAddWhileLoop(3,2) =", multByAddWhileLoop(3,2))

