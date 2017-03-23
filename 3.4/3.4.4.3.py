from string import ascii_lowercase

def main():
	print ascii_lowercase
	print zip(ascii_lowercase, range(1,27))
	print dict(zip(ascii_lowercase, range(1,27)))

	print sorted(dict(zip(ascii_lowercase, range(1,27))).items())

if __name__ == '__main__':
	main()
