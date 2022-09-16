my_friend = {'first_name': 'mike', 'last_name': 'beckham',
             'age': 36, 'city': 'austin'}

# print(f"{my_friend['first_name'].title()} {my_friend['last_name'].title()} is "
#       f"a {my_friend['age']}-year-old from {my_friend['city']}.")

person_1 = {'first_name': 'jeff', 'last_name': 'jefferson', 'age': 80, 'city': 'austin'}
person_2 = {'first_name': 'jim', 'last_name': 'smith', 'age': 42, 'city': 'dallas'}

people = [person_1, person_2, my_friend]

for person in people:
    # print(f"{person['first_name'].title()} {person['last_name'].title()} is"
    #       f" a {person['age']}-year-old from {person['city']}.")
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"{full_name} is a {person['age']}-year-old from {person['city']}.")

