def make_car(manufacturer, model, **known_car_info):
    """Stores information about a car in a dictionary."""
    known_car_info['manufacturer'] = manufacturer
    known_car_info['model'] = model
    return known_car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

