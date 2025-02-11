kata = (19, 42, 21)

def format_tuple(kata):
	result = ", ".join(map(str, kata))

	print(f"The {len(kata)} numbers are: {result}")

if __name__ == "__main__":
	format_tuple(kata)
