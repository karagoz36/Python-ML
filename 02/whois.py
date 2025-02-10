import sys

def check(number):
	if number == 0:
		return "I'm zero."
	elif number % 2 == 0:
		return "I'm even."
	else:
		return "I'm odd."

def main():
	if len(sys.argv) == 2:
		try:
			number = int(sys.argv[1])
			print(check(number))
		except ValueError:
			print("The number you provided is not an integer!")
	else:
		print("Usage: One integer arguments please!")

if __name__ == "__main__":
	main()
