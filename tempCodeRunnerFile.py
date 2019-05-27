import re
text = 'ha hahaha ha'
pattern = re.compile(r'/bha')

matches = pattern.finditer(text)
print(matches)
