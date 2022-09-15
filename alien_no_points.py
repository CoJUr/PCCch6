alien_0 = {'colr': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# to get around the error, use the get() method. pass the key you want and a
# default return value as 2nd arg if the key doesn't exist.

point_value = alien_0.get('points', 'no point value designated')
print(point_value)
# good to use get() if unsure the key exists in the dict


