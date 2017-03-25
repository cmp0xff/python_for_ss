#!/usr/bin/python -tt

def main():
	responses = ['Y', 'Yes', 'No', 'no', '', 'Yep']
	responses = [x[0].lower() if x else 'n' for x in responses]
	print responses

if __name__ == '__main__':
	main()
