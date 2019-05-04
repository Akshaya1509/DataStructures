# Check if 2 strings are permutations of each other
# this works for case sensitive as well


def check_permutation(s1, s2):
	d = {}
	if len(s1) != len(s2):
		return False
	for ch in s1:
		val = ord(ch)
		if val not in d:
			d[val] = 1
		else:
			d[val] += 1
	for ch in s2:
		val = ord(ch)
		if val not in d:
			return False
		d[val] -= 1
	val_set = set(d.values())
	if len(val_set) > 1 or val_set.pop() != 0:
		return False
	return True


print(check_permutation('ak', 'ka'))  # True
print(check_permutation('apple', 'orange'))  # False
print(check_permutation('  ', '  ')) #True
print(check_permutation('a_$% k', '_$%k a')) #True
print(check_permutation('God', 'god')) #False
