# Script to check if string has uniq chars


def is_unique(s):
    d = {}
    isUnique = True
    for ch in s:
        v = ord(ch)
        if v not in d:
            d[v] = 1
        else:
            isUnique = False
            break
    return isUnique


def is_unique_without_storage(s):
    isUnique = True
    s = sorted(s)
    prev = s[0]
    for ch in s[1:]:
        if prev == ch:
            isUnique = False
            break
        prev = ch
    return isUnique


# print(is_unique('abcd')) #True
# print(is_unique('abddcd')) #False
# print(is_unique('acbccd')) #False
# print(is_unique('a bd')) #True
# print(is_unique('    ')) #False

print(is_unique_without_storage('abcd')) #True
print(is_unique_without_storage('abddcd')) #False
print(is_unique_without_storage('acbccd')) #False
print(is_unique_without_storage('a bd')) #True
print(is_unique_without_storage('    ')) #False