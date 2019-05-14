# Check if 2 strings are 0/1 edit away 
# edit : insert a char, remove a char or replace a char

def count_occurrence(s):
    d = {}
    for i in s:
        if ord(i) not in d:
            d[ord(i)] = 1
        else:
            d[ord(i)] += 1
    return d

def one_away(s1, s2):
    if s1 == s2:
        return True
    d = count_occurrence(s1)
    count = 0
    for i in s2:
        if count > 1:
            return False
        if ord(i) not in d:
            count += 1
        if i in d:
            d[ord(i)] -= 1
    s = set(d.values())
    return count <= 1 and len(s) == 1 and s.pop() == 1

print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))

    
    