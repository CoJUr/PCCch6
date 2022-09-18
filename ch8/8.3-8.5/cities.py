def describe_city(city_name, country='SomeLand'):
    """Display a city and its country."""
    print(f"{city_name.title()} is in {country.title()}.")

describe_city('paris', 'france')
describe_city('new york', 'united states')
describe_city('tokyo', 'japan')
describe_city('prague')

