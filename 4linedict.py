from re import findall
s = input("Your Word: ")
y = len(findall("(?=bob)", s))
print(y)
