def city_country(city, country):
    """Take in a city and country, return the formatted location string."""
    city_name = city
    country_name = country

    return f"{city_name.title()}, {country_name.title()}"


someplace_in_tx = city_country('houston', 'united states of america')
print(someplace_in_tx)

someplace_in_germany = city_country('berlin', 'germany')
print(someplace_in_germany)

print(city_country('paris', 'france'))




