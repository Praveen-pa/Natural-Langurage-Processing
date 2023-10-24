irregular_nouns = {'man': 'men', 'woman': 'women', 'child': 'children'}

words_to_pluralize = ['cat', 'dog', 'man', 'woman', 'bus', 'box', 'church']

for word in words_to_pluralize:
    if word in irregular_nouns:
        plural_form = irregular_nouns[word]
    elif word.endswith('s') or word.endswith('x') or word.endswith('z'):
        plural_form = word + 'es'
    else:
        plural_form = word + 's'
    
    print(f'Plural of {word}: {plural_form}')
