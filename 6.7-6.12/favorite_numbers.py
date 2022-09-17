favorite_numbers = {
    'josh': [7, 9, 11],
    'carl': [3, 5, 7],
    'sam': [2, 4, 3],
    'becky': [4, 5, 6],
}

# for favorite_number in favorite_numbers:
#     print(f"{favorite_number.title()}'s favorite number"
#           f" is {favorite_numbers[favorite_number]}.")

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")


