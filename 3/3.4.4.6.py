def main():
	from collections import Counter
	# Tally occurrences of words in a list
	cnt = Counter()
	for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
		cnt[word] += 1
	print cnt

	from urllib2 import urlopen
	hamlet_url = 'http://www.gutenberg.org/ebooks/1524.txt.utf-8'
	hamlet_text = urlopen(hamlet_url).read()
	import re
	hamlet_words_re = re.findall(r'\w+', hamlet_text.lower())
	hamlet_words = hamlet_text.lower().split()
	print 'Hamlet using re: ', Counter(hamlet_words_re).most_common(10)
	print 'Hamlet using split: ', Counter(hamlet_words_re).most_common(10)

	pride_url = 'http://www.gutenberg.org/files/1342/1342-0.txt'
	pride_text = urlopen(pride_url).read()
	pride_freq = Counter(pride_text.lower().split())
	print 'Pride using split: ', pride_freq.most_common(50)
	
if __name__ == '__main__':
	main()
