def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# redefine to print a sentence with the toppings separately via a for loop
def make_pizza(*toppings):
    """Summarize the pizza we will make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

