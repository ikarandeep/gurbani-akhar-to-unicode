# -*- coding: utf-8 -*-
import codecs


def convert(letter):
	gurmukhi_english = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"," ","1","2","@","3","4","5","6","^","7","&","8","9","0","[","]","<",">"]
	#gurmukhi_unicode = ["ੳ","ਆ","ਬ","ਭ","ਚ","ਛ","ਦ","ਧ","ੲ","ਓ","ਡ","ਢ","ਗ","ਘ","ਹ","੍ਹ","ਿ","ੀ","ਜ","ਝ","ਕ","ਖ","ਲ","ਲ਼","ਮ","ੰ","ਨ","ਂਂ","ੋ","ੌ","ਪ","ਫ","ਤ","ਥ","ਰ","੍","ਸ","ਸ਼","ਟ","ਠ","ੁ","ੂ","ਵ","ੜ","ਾ","ਾਂ","ਣ","ਯ","ੇ","ੈ","ਜ਼","ਗ਼"," ","੧","੨","ਹ੍ਹ","੩","੪","੫","੬","ਖ਼","੭","ਫ਼","੮","੯","੦","।","॥"]
	gurmukhi_unicode = [u"ੳ",u"ਆ",u"ਬ","ਭ",u"ਚ",u"ਛ",u"ਦ",u"ਧ",u"ੲ",u"ਓ",u"ਡ",u"ਢ",u"ਗ",u"ਘ",u"ਹ",u"੍ਹ",u"ਿ",u"ੀ",u"ਜ",u"ਝ",u"ਕ",u"ਖ",u"ਲ",u"ਲ਼",u"ਮ",u"ੰ",u"ਨ",u"ਂਂ",u"ੋ",u"ੌ",u"ਪ",u"ਫ",u"ਤ",u"ਥ",u"ਰ",u"੍",u"ਸ",u"ਸ਼",u"ਟ",u"ਠ",u"ੁ",u"ੂ",u"ਵ",u"ੜ",u"ਾ",u"ਾਂ",u"ਣ",u"ਯ",u"ੇ",u"ੈ",u"ਜ਼",u"ਗ਼",u"\u0020",u"੧",u"੨",u"ਹ੍ਹ",u"੩",u"੪",u"੫",u"੬",u"ਖ਼",u"੭",u"ਫ਼",u"੮",u"੯",u"੦",u"।",u"॥",u"ੴ",u">"]
	return gurmukhi_unicode[gurmukhi_english.index(letter)]



def convertLine(line):
	unicode_list = []
	# if the tukh has "ir", we should swap the characters or else the output is incorrect
	for i in range(len(line)):
		index_to_convert = i
		converted_letter = convert(line[index_to_convert])
		unicode_list.append(converted_letter)
		if unicode_list[i-1] == u"ਿ" and unicode_list[i] == u"ਰ":
			temp = unicode_list[i]
			unicode_list[i] = unicode_list[i-1]
			unicode_list[i-1] = temp
	
	return "".join(unicode_list)

def main():
	line = raw_input()
	print convertLine(line)



if __name__ == 	"__main__":
	main()
