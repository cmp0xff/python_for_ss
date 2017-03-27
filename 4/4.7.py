#!/usr/bin/python -tt

# Exercise 9
def add1(x):
	return x+1

#Exercise 10
def fahrenheit_to_celsius(x):
	return (x-32)*5/9.

def cone_volume(r,h):
	import math
	return r * r * h * math.pi / 3.

def main():
	a_list = [2,7,8,19]
	# Exercise 1
	print a_list[0]
	# Exercise 2
	print a_list[-1]
	# Exercise 3
	print a_list[1:-1]
	# Exercise 4
	print [x+1 for x in a_list]
	# Exercise 5
	print [x<8 for x in a_list]

	test_list = ['the', 'be', 'of', 'and', 'a', 'in', 'to', 'have', 'it',
		'to', 'for', 'I', 'that', 'you', 'he', 'on', 'with', 'do',
		'at', 'by', 'not', 'this', 'but', 'from', 'they', 'his']
	# Exercise 6
	result = {word for word in test_list if len(word) == 3}
	print result
	# Exercise 7
	three_let_word_freq = 0
	for word in test_list:
		if len(word) == 3:
			three_let_word_freq += 1
	print three_let_word_freq

	L = ['1', '4', '1', '5', '9', '2', '6', '5', '3', '5',
		'8', '9', '7', '9', '3', '1', '1', '6']
	# Exercise 8
	import collections
	freq_L = collections.Counter()
	for ele in L:
		freq_L[ele] += 1
	print freq_L.most_common(1)

	#Exercise 9
	print add1(2)
	#Exercise 10
	print fahrenheit_to_celsius(212), fahrenheit_to_celsius(-40),\
		fahrenheit_to_celsius(32)
	#Exercise 11
	print cone_volume(2,3)

if __name__ == '__main__':
	main()
