topping_to_add = input("Enter a pizza topping: ")

toppings = []

while True:
    if topping_to_add == 'quit':
        print("making your pizza with the following toppings:")
        for topping in toppings:
            print(f"\t{topping}")
        break

    toppings.append(topping_to_add)
    print(
        f"Added {topping_to_add} to your pizza. If you're done, enter 'quit'.")

    topping_to_add = input("Enter a pizza topping: ")



