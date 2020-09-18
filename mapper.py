import output

keywords = {
	'cowk':'coke',
	'coke':'coke',
	'mate':'mate',
	'marta':'mate',
	'hackathon':'hackathon',
	'hackasin':'hackathon',
	'hekesin': 'hackathon'
}

keyword_to_fun = {
	'coke' : 'led_on',
	'mate' : 'dont_puke',
	'hackathon' : 'puke'
}

def get_keywords():
	def gen_kw_entries(keys, sensitivity):
		return [(k,sensitivity) for k in keys]

	return gen_kw_entries(keywords.values(),0.2)

def word_found(word):
	if word in keywords:
		keyword_found(keywords[word])


def keyword_found(kw):
	eval("output."+keyword_to_fun[kw]+"()")
