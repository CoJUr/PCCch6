cities = {
    'santiago': {
        'country': 'chile',
        'population': 5000000,
        'fact': 'Santiago is the capital of Chile.',
        },
    'new york': {
        'country': 'united states',
        'population': 8000000,
        'fact': 'New York is the most populous city in the United States.',
        },
    'paris': {
        'country': 'france',
        'population': 2000000,
        'fact': 'Paris is the capital of France.',
        }

    }

for city, info in cities.items():
    city = city.title()
    country = info['country'].title()
    population = info['population']
    fact = info['fact']

    print(f"\n{city} is in {country}.")
    print(f"It has a population of {population}.")
    print(f"{fact}")
print("###########")
# extension 6.12
cities.update({'austin': {'country': 'united states', 'population': 1000000, 'fact': 'Austin is the capital of Texas.'}})

for city, info in cities.items():
    print(f"\n{city.title()} is in {info['country'].title()}.")
    print(f"It has a population of {info['population']}.")
    print(f"{info['fact']}")

