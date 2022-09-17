sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("The following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

