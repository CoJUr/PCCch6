# remove() method is best for removing a unique item from a list
# to remove all instances of a value from a list, can use a while loop

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


