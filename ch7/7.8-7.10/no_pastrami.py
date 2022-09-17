sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print(f"The following sandwiches have been made:"
      f"{finished_sandwiches}")

