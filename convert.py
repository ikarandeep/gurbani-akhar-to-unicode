# -*- coding: utf-8 -*-

def convert(letter):
	gurmukhi_english = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"," ","1","2","@","3","4","5","6","^","7","&","8","9","0","[","]"]
	gurmukhi_unicode = [u"ੳ",u"ਆ",u"ਬ","ਭ",u"ਚ",u"ਛ",u"ਦ",u"ਧ",u"ੲ",u"ਓ",u"ਡ",u"ਢ",u"ਗ",u"ਘ",u"ਹ",u"੍ਹ",u"ਿ",u"ੀ",u"ਜ",u"ਝ",u"ਕ",u"ਖ",u"ਲ",u"ਲ਼",u"ਮ",u"ੰ",u"ਨ",u"ਂਂ",u"ੋ",u"ੌ",u"ਪ",u"ਫ",u"ਤ",u"ਥ",u"ਰ",u"੍",u"ਸ",u"ਸ਼",u"ਟ",u"ਠ",u"ੁ",u"ੂ",u"ਵ",u"ੜ",u"ਾ",u"ਾਂ",u"ਣ",u"ਯ",u"ੇ",u"ੈ",u"ਜ਼",u"ਗ਼",u" ",u"੧",u"੨",u"ਹ੍ਹ",u"੩",u"੪",u"੫",u"੬",u"ਖ਼",u"੭",u"ਫ਼",u"੮",u"੯",u"੦",u"।",u"॥"]
	return gurmukhi_unicode[gurmukhi_english.index(letter)]



shabad = raw_input()
shabad_unicode = []

# if the tukh has "hi", we should move it to after the character
for i in range(len(shabad)):
	index_to_convert = i
	shabad_unicode.append(convert(shabad[index_to_convert]))
	if shabad_unicode[i-1] == u"ਿ" and shabad_unicode[i] == u"ਰ":
		temp = shabad_unicode[i]
		shabad_unicode[i] = shabad_unicode[i-1]
		shabad_unicode[i-1] = temp

print "".join(shabad_unicode)