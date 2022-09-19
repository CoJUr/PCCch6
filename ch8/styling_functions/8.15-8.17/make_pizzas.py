def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nThe {size}-inch pizza with toppings:")
    for topping in toppings:
        print(f"- {topping}")

    print(" is ready!")