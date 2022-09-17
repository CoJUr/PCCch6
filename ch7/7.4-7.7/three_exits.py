# user_age = ""
#
# while user_age != 'quit':
#     user_age = input("How old are you? ")
#     if user_age == 'quit':
#         break
#     elif int(user_age) < 3:
#         print("Your ticket is free.")
#     elif 3 <= int(user_age) <= 12:
#         print("Your ticket is $10.")
#     elif int(user_age) > 12:
#         print("Your ticket is $15.")
#

price = 15

while True:
    message = input("How old are you? "
                    "Enter 'quit' to quit. ")
    if message == 'quit':
        break
    age = int(message)

    if age < 3:
        price = 0
        print(f"Your ticket is ${price}.")
        continue
    elif 3 <= age <= 12:
        price = 10
        print(f"Your ticket is ${price}.")
        continue
    elif age > 12:
        # price = 15
        print(f"Your ticket is ${price}.")
        continue

