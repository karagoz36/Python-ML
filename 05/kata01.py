kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

def display(kata):
	for x, y in kata.items():
		print(f"{x} was created by {y}")

if __name__ == "__main__":
	display(kata)
