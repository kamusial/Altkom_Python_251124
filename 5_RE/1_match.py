import re

pattern = r'a'
text = 'abc'
match = re.match(pattern, text)
print(match.group())

pattern = r'a.b'
text = 'acb'
match = re.match(pattern, text)
print(match.group())

pattern = r'ab*c'
text = 'abbbbcwewe'
match = re.match(pattern, text)
print(match.group())

# pattern = r'ab?c'
# text = '3acwewe'
# match = re.match(pattern, text)
# print(match.group())

