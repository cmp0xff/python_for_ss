#!/usr/bin/python -tt

import collections

def main():
	file_str = open('1342-0.txt', 'r').read()
	print len(file_str)
	print len(file_str.split())
	file_lines = open('1342-0.txt', 'r').readlines()
	print len(file_lines)
	print file_lines[len(file_lines)/2]

	ofh = open('foo.txt','w')
	print >> ofh, 'Great news'
	print >> ofh, "Monty Python lives!"
	print >> ofh, 'Hooray!'
	ofh.close()

	ctr = collections.Counter()
	token_ctr = 0

	with open('1342-0.txt', 'r') as file_handle:
		for line in file_handle:
			line_words = line.strip().split()
			for word in line_words:
				token_ctr += 1
				ctr[word] += 1

	print len(ctr), token_ctr, sum(ctr.values())

	ctr4 = collections.Counter(open('1342-0.txt', 'r').read().split())
	print len(ctr4), sum(ctr.values())

if __name__ == '__main__':
	main()