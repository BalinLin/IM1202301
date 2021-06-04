def decoding(data, text):
	s = ""
	for i in data:
		s += text[int(i)]
	return s