def words(string):
	worddict={}
	result=string.split()

	for word in result:
		if word.isdigit():
			count = result.count(word)
			worddict[int(word)] = word

		else:
			count = result.count(word)
			worddict[word] = word

	return result




	




