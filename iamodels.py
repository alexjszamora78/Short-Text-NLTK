from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import os

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

if not os.path.exists("output"):
	os.mkdir("output")

def short_text(size,average,sentences,sentenceValue):
	threshold = size * average
	summary = ''
	for sentence in sentences:
		if (sentence in sentenceValue) and (sentenceValue[sentence] > threshold): #(1.2 * average)):
			summary += " " + sentence

	return summary

def Short_Text_Model(txt_file,languaje,size):
	SW = set(stopwords.words(languaje))
	text = open(txt_file, 'r').read()
	words = word_tokenize(text)
	freqTable = dict()

	for word in words:
		word = word.lower()
		if word in SW: 
			continue
		if word in freqTable:
			freqTable[word] += 1
		else:
			freqTable[word] = 1

	sentences = sent_tokenize(text)
	sentenceValue = dict()

	for sentence in sentences:
		for word, freq in freqTable.items():
			if word in sentence.lower():
				if sentence in sentenceValue:
					sentenceValue[sentence] += freq
				else:
					sentenceValue[sentence] = freq

	sumValues = 0
	for sentence in sentenceValue:
		sumValues += sentenceValue[sentence]
	    
	average = int(sumValues/ len(sentenceValue))
	status = True

	while True:
		summary = short_text(size,average,sentences,sentenceValue)
		if len(summary) != 0:
			size += 0.1
		else:
			size -= 0.1
			summary = short_text(size,average,sentences,sentenceValue)
			break

	print("Rango final",str(size)[:4])

	with open("output/resumen.txt","w") as txt:
		txt.write(summary)

	print("Resumen guardado en la ruta output/resumen.txt")