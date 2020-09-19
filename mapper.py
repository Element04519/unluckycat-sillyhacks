import output


bullshit_words = {"agile", "modular", "blockchain", "crypto", "bitcoin", "tesla", "AI"}
good_words = {"coke", "mate", "hackathon", "hackspace", "hacker", "python"}
bad_words = {"beer", "wine", "party", "marketing", "ads", "advertisment", "sun", "birds", "daylight", "javascript", "php"}

keyword_dict = dict()
for w in bullshit_words:
	keyword_dict[w] = "bullshit"
for w in good_words:
	keyword_dict[w] = "good"
for w in bad_words:
	keyword_dict[w] = "bad"

def keyword_found(kw):
	pass
	
