"""
Basic Python examples: hello world, variables, functions, loops, classes.

Run: python index.py
"""

def hello():
	print("Hello, world!")


def add(a, b):
	"""Return the sum of a and b."""
	return a + b


def loop_example(n=3):
	for i in range(n):
		print(f"Loop iteration: {i}")


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def greet(self):
		print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


if __name__ == "__main__":
	hello()
	print("Add 2 + 3 =", add(2, 3))
	loop_example(3)
	p = Person("Alice", 30)
	p.greet()


return 0;