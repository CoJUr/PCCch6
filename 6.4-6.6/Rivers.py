major_rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    }

for river in major_rivers:
    print("The " + river.title() + " runs through " + major_rivers[
        river].title() + ".")

# for river in major_rivers: to print the keys (default)
for river in major_rivers:
    print(river.title())

# for country in major_rivers.values():
for river in major_rivers:
    print(major_rivers[river].title())



