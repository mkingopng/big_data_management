from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")
DATE_RE = re.compile(r'^[0-9]{8}$')


class MRMostUsedWord(MRJob):
	
	def steps(self):
		return [
			MRStep(
				mapper=self.mapper_get_date,
				mapper=self.mapper_get_words,
				combiner=self.combiner_count_words,
				reducer=self.reducer_count_words),
			MRStep(reducer=self.reducer_find_max_word)
		]
	
	def mapper_get_date(self, _, line):
		for date in DATE_RE.findall(line):
			yield date
	
	def mapper_get_words(self, _, line):
		# yield each word in the line
		for word in WORD_RE.findall(line):
			yield word.lower(), 1
	
	def combiner_count_words(self, word, counts, date):
		# optimization: sum the words we've seen so far
		yield date, word, sum(counts)
	
	def reducer_count_words(self, date, word, counts):
		# send all (num_occurrences, word) pairs to the same reducer.
		# num_occurrences is so we can easily use Python's max() function.
		yield date, sum(counts), word
	
	# discard the key; it is just None
	def reducer_find_max_word(self, _, date, word_count_pairs):
		# each item of word_count_pairs is (count, word),
		# so yielding one results in key=counts, value=word
		yield date, max(word_count_pairs)


if __name__ == '__main__':
	MRMostUsedWord.run()

# python mr_word_count.py abcnews.txt
