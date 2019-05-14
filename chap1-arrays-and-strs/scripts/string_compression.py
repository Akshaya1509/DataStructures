# Check if length of compressed string is greater than original string length
# Compressed : aabbcdd - a2b2c1d2
# Assumption :  String contains only UpperCase and LowerCase chars

def get_compressed_len(s):
    comp_len = 0
    count = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            comp_len += 1 + len(str(count))
            count = 1
        else:
            count += 1
    return comp_len + 1 + len(str(count))

def compress_string(s):
    if s.strip() == "" or s == None:
        return
    comp_len = get_compressed_len(s)
    if comp_len >= len(s):
        return s
    count = 1
    comp = []
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            comp.append(s[i] + str(count))
            count = 1
        else:
            count += 1
    comp.append(s[-1] + str(count))
    comp_str = ''.join(comp)
    return comp_str

print(compress_string("aabcccccaaabzzq"))
    