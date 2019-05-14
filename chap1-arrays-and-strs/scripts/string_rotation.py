# Assuming we have a isSubstring method, 
# to check is one string is a rotation of other by making only ONE call to isSubstring

def isRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        # assuming find is isSubstring
        if s1s1.find(s2):
            return True
        return False

print(isRotation("waterbottle", "erbottlewat"))