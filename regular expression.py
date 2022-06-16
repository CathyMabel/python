import re
str="python programming with frameworkS"
pattern='g$'
match=re.findall(pattern,str)
print(match)