import sys

def reverse_swap_case(input_str):
	return input_str[::-1].swapcase()

def main():
	n = len(sys.argv)
	if n >= 2:
		if n == 2:
			input_str = sys.argv[1]
		else:
			input_str = " ".join(sys.argv[1:])
		print(reverse_swap_case(input_str))
	else:
		print("Usage: python exec.py <input_string>")

if __name__ == "__main__":
	main()
