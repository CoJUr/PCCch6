# loops with lists and dictionaries - shouldnt modify a list inside a for
# loop bc pythong will have trouble keeping track of the items in the list.
# use a while loop with lists/dicts instead to work with items

# moving items from one list to another
# start with users that need to be verified, and an empty list to hold
# confirmed users. verify each user until there are no more unconfirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")

    confirmed_users.append(current_user)

# display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())