bird = {
    'kind': 'parrot',
    'name': 'Polly',
    'owner_name': 'joe',
    }

dog = {
    'kind': 'pug',
    'name': 'Buddy',
    'owner_name': 'myself',
    }

cat = {
    'kind': 'tabby',
    'name': 'Mittens',
    'owner_name': 'jim',
    }

pets = [bird, dog, cat]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']} and is owned by "
          f"{pet['owner_name'].title()}.")

