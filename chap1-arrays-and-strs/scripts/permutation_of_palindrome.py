# Check if a string is permutation of palindrome

def count_occurrences(s):
	d = {}
	for ch in s:
		v = ord(ch)
		if v not in d:
			d[v] = 1
		else:
			d[v] += 1
	return d

def permutation_of_palindrome(s):
	if s == None or s == "":
		return
	s = s.lower()
	s = s.replace(" ", "")
	print(s)
	count = 0
	d = count_occurrences(s)
	print(d)
	values = d.values()
	for i in values:
		if i % 2 != 0:
			count += i
	if count > 1:
		return False
	return True

def permutation_of_palindrome2(s):
	if s == None or s == "":
		return 
	s = s.lower()
	s = s.replace(" ", "")
	d = {}
	odd_count = 0
	for ch in s:
		v = ord(ch)
		if v not in d:
			d[v] = 1
			odd_count +=1
		else:
			d[v] += 1
			if d[v] % 2 == 0:
				odd_count -= 1
			else:
				odd_count += 1
	return odd_count <= 1 



# print(permutation_of_palindrome('daamm')) #True
# print(permutation_of_palindrome('daamme')) #False
# print(permutation_of_palindrome('    ')) #True
# print(permutation_of_palindrome(' b ')) #True
# print(permutation_of_palindrome(' b n')) #False
# print(permutation_of_palindrome('Tact coa')) #True

print(permutation_of_palindrome2('daamm')) #True
print(permutation_of_palindrome2('daamme')) #False
print(permutation_of_palindrome2('    ')) #True
print(permutation_of_palindrome2(' b ')) #True
print(permutation_of_palindrome2(' b n')) #False
print(permutation_of_palindrome2('Tact coa')) #True
