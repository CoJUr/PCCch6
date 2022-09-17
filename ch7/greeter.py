# name = input("Please enter your name: ")

# building a multi-line string
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}!")

age = input("How old are you? ")
age = int(age)
print(age >= 18)
