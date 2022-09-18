def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')


    # passing arguments - positionals, keywords; lists and dictionaries

# positional arguments - must be in the same order the parameters were defined
def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet('hamster', 'harry')

# describe_pet('dog', 'willie')


    # keyword arguments - keyword args passed in the function call
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# default values - if an argument for a parameter is not provided in the call,
# the parameter will be assigned its default value. simplifies function calls

def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet, of default type dog."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
# default parameter values always defined after non-default parameters


# equivalent function calls for a dog named willie
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='willie', animal_type='dog')


# avoiding argument errors - unmatched arguments, missing arguments
describe_pet() # TypeError: describe_pet() missing 1 required positional arg









