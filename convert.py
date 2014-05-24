# -*- coding: utf-8 -*-

def convert(letter):
	gurmukhi_english = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"," "]
	gurmukhi_unicode = [u"ੳ",u"ਆ",u"ਬ","ਭ",u"ਚ",u"ਛ",u"ਦ",u"ਧ",u"ੲ",u"ਓ",u"ਡ",u"ਢ",u"ਗ",u"ਘ",u"ਹ",u"੍ਹ",u"ਿ",u"ੀ",u"ਜ",u"ਝ",u"ਕ",u"ਖ",u"ਲ",u"ਲ਼",u"ਮ",u"ੰ",u"ਨ",u"ਂਂ",u"ੋ",u"ੌ",u"ਪ",u"ਫ",u"ਤ",u"ਥ",u"ਰ",u"੍",u"ਸ",u"ਸ਼",u"ਟ",u"ਠ",u"ੁ",u"ੂ",u"ਵ",u"ੜ",u"ਾ",u"ਾਂ",u"ਣ",u"ਯ",u"ੇ",u"ੈ",u"ਜ਼",u"ਗ਼"," "]
	return gurmukhi_unicode[gurmukhi_english.index(letter)]



shabad = raw_input()
shabad_unicode = []
for letter in shabad:
	shabad_unicode.append(convert(letter))

print "".join(shabad_unicode)