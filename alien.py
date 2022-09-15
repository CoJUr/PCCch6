alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You earned {new_points} points!")

# can add new key-value pairs to a dictionary at any time. theyre dynamic

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print(f"The color of the alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien changed to color {alien_0['color']}.")

print("##########")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original (x) position: {alien_0['x_position']}")

# move alien to the right, determining how far based on current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:  # fast alien
    x_increment = 3

# new position = old position + increment
alien_0['x_position'] += x_increment

print(f"New X position of the {alien_0['speed']} speed alien is:"
      f" {alien_0['x_position']}")

# using del to remove a key-value pair from a dictionary. pass the name of
# the dict and key you want to remove

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# using a dict to store similar infor about many objects, like a poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


