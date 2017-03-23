from example_string import example_string

count_dict = dict()
words_freq = list()

def main():

	for word in example_string.split():
		while len(word) != 1 and not word[0].isalpha():
			word = word[1:]
		while len(word) != 1 and not word[-1].isalpha():
			word = word[:-1]

		word = word.lower()

		if word in count_dict:
			count_dict[word] += 1
		else:
			count_dict[word] = 1

	print count_dict

	for (word, count) in count_dict.items():
		words_freq.append((count, word))

	print sorted(words_freq, reverse = True)

if __name__ == '__main__':
	main()
