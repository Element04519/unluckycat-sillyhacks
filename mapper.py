keywords = {
	'cowk':'coke',
	'coke':'coke',
	'mate':'mate',
	'marta':'mate',
	'hackathon':'hackathon',
	'hackasin':'hackathon',
	'hekesin': 'hackathon'
}

def get_keywords():
	def gen_kw_entries(keys, sensitivity):
		return [(k,sensitivity) for k in keys]

	return gen_kw_entries(keywords.values(),0.2)

def word_found(word):
	if word in keywords:
		keyword_found(keywords[word])


def keyword_found(kw):
	#TODO map here
	print(kw)
	pass