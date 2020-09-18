import output



keyword_to_fun = {
	'coke' : output.led_on,
	'mate' : output.dont_puke,
	'hackathon' : output.puke
}

def get_keywords():
	return keyword_to_fun.keys()


def word_found(word):
	if word in keyword_to_fun.keys():
		keyword_found(word)


def keyword_found(kw):
	print(kw)
	keyword_to_fun[kw]()
