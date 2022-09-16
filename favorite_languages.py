favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# keys() method for a dictionary returns a list of all keys in the dictionary

# for name in favorite_languages.keys():
#     print(name.title())

# looping through keys is default behavior, so .keys() call is optional

for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take the poll!")

# sorted() function returns a sorted copy of the list, original list unchanged
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# values() method returns a list of values without any keys. doesn't check for
# duplicate values. use a set() to get a list of unique values
print("These languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

# can build a set directly using braces and separating items with commas
languages = {'python', 'ruby', 'python', 'c'}

print(languages)

people_to_poll = ['jen', 'sarah', 'edward', 'erin', 'jim', 'joe']

for name in people_to_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, please take the poll!")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are: ")
        for language in languages:
            print(f"{language.title()}")
    else:
        for language in languages:
            print(f"\n{name.title()}'s favorite language is {language.title()}")

