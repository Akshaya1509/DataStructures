# Urlify a given string - replace spaces with %20

def urlify(s):
	if s == None or s == "":
		return 
	url = []
	for ch in s:
		if ch == ' ':
			url.append("%20")
		else:
			url.append(ch)
	return ''.join(url)

print(urlify('jones smith'))
print(urlify(None))
print(urlify('Smith  '))
print(urlify('   '))