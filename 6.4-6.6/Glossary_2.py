programming_words = {
    'dictionary': 'A collection of key-value pairs.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'elif': 'An abbreviation of "else if", used in conditional statements.',
    'list': 'A collection of items in a particular order.',
}
#
# for word, definition in programming_words.items():
#     print(f"{word.title()}: {definition}\n")

programming_words['loop'] = 'The action of doing something over and over again.'
programming_words['set'] = 'A collection in which each item must be unique.'
programming_words['if'] = 'A conditional test that determines whether a block of code will be executed.'
programming_words['else'] = 'A block of code that will be executed if the conditional test fails.'
programming_words['tuple'] = 'An immutable list.'
programming_words['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in programming_words.items():
    print(f"{word.title()}: {definition}\n")
