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


# mixing positional and arbitrary arguments - the arbitrary arg comes last
def make_pizza(size, *toppings):
    """summarize the pizza we're about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

