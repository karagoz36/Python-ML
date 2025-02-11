import sys

def operations(a,b):
	print(f"Sum: {a + b}")
	print(f"Difference: {a - b}")
	print(f"Product: {a * b}")

	if b == 0:
		print("Quotient: ERROR (division by zero)")
		print("Remainder: ERROR (modulo by zero)")
	else:
		print(f"Quotient: {a / b}")
		print(f"Remainder: {a % b}")

def main():
	if len(sys.argv) > 3:
		print("AssertionError: too many arguments")
		return
	elif len(sys.argv) < 3:
		print("Usage: python operations.py <number1> <number2>")
		print("Example:\n	python operations.py 10 3")
		return
	try:
		n1 = int(sys.argv[1])
		n2 = int(sys.argv[2])
	except ValueError:
		print("AssertionError: only integers")
		return
	operations(n1, n2)

if __name__ == "__main__":
	main()
