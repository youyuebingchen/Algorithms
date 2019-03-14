import re
pattern = re.compile(r"[a-z]*")
obj = pattern.search("you are 是最好 the best!")
print(obj.span())
print(obj.group())