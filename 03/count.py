import sys
import string

def text_analyzer(txt=None):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if txt is None:
		txt = input("Please put the text to analyze!\n")

	if not isinstance(txt, str):
		raise AssertionError("Argument is not a string!")

	char_count = len(txt)
	upper_count = sum(1 for char in txt if char.isupper())
	lower_count = sum(1 for char in txt if char.islower())
	punc_count = sum(1 for char in txt if char in string.punctuation)
	space_count = sum(1 for char in txt if char.isspace())

	print(f"The text contains {char_count} printable character(s):")
	print(f"- {upper_count} upper letter(s)")
	print(f"- {lower_count} lower letter(s)")
	print(f"- {punc_count} punctuation mark(s)")
	print(f"- {space_count} space(s)")


def main():
	if len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		print("Error")

if __name__ == "__main__":
	main()
