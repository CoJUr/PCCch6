def build_profile(first, last, **user_info):
    """Build a dict containing all we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

my_profile = build_profile('cory', 'urton',
                           location='TX',
                           field='software development',
                           pet_dog='leon')

print(my_profile)
