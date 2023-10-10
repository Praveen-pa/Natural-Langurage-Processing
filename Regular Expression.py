import re
text=" Regulae expression are the powerful tool for text processing"
word_pattern=r'\w+'
word=re.findall(word_pattern,text)
print(word)