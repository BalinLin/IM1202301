def getset(mystring):
    return set(mystring)

def IoU(myset1, myset2):
    return len(myset1 & myset2) / len(myset1 | myset2)

def percentage(myset, mystring):
    return len(myset & set(mystring)) / len(mystring) * 100

def removefist(mystring):
    myset = set()
    output = ""
    for i in mystring:
        if i in myset: output += i
        else: myset.add(i)
    return output