kata = (2019, 9, 25, 3, 30)

def display_date(kata):
	print(f"{kata[1]:02d}/{kata[2]:02d}/{kata[0]:04d} {kata[3]:02d}:{kata[4]:02d}")

if __name__ == "__main__":
	display_date(kata)
