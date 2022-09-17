vacation_poll = {}

prompt = "if you could visit one place in the world, where would you go? "

while True:
    name = input("what is your name? ")
    response = input(prompt)
    vacation_poll[name] = response

    repeat = input("would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        break

print("--- Poll Results ---")
for name, response in vacation_poll.items():
    print(f"{name} would like to visit {response}.")