favorite_plaes = {
    'jim': ['new york', 'paris', 'london'],
    'joe': ['austin', 'dallas', 'houston'],
    'jane': ['san francisco', 'los angeles', 'san diego'],
    }

for name, places in favorite_plaes.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
        