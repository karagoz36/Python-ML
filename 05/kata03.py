kata = "The right format"

def format_string(kata):
	formatted = kata.rjust(42, '-')
	print(formatted, end="")

if __name__ == "__main__":
	format_string(kata)
