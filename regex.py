import re

text = "Aditya Narayan Mishra"
text2 = '''Mahesh Prasad abc... mishra!@^%$*#
dsf

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

cat
mat
pat
bat

Mr. Scahfer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
text3 = 'www.adityanarayanmishra.me'
sentence = 'Start a sentence and then bring it to an end'
email = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
# r'M(r|s|rs)\.?\s[A-Z]\w*'
# r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
#matches = pattern.finditer(email)

# with open('data.txt', 'r') as f:
#     contents = f.read()
matches = pattern.finditer(email)
for match in matches:
    print(match)
