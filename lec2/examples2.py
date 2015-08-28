import doctest
# nested functions and environments
def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    def h(x):
        if x < b:
            return f(x)
        else:
            return g(x)
    return h

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    def func(x):
        total = f(x)
        for num in range(1, n):
            total = f(total)
        return total
    return func

# recursion
def countdown(n):
	"""Return the countdown sequence from n to 0.

	>>> countdown(5)
	5
	4
	3
	2
	1
	0
	"""
	print(n)
	if (n == 0):
		return
	else:
		return countdown(n - 1)

def factorial(n):
	"""Return n!.
	>>> factorial(5)
	120
	>>> factorial(4)
	24
	"""
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

def fib(n):
	"""Return the nth fibonacci number

	>>> fib(5)
	5

	"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

doctest.testmod()
