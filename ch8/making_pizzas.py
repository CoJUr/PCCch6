# import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# can also import as many specific functions as you want like this:
# from module_name import function_0, function_1, function_2

# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# using 'as' to give a function an alias: if e.g. potential name conflict
# from module_name import function_name as fn

# from pizza import make_pizza as mp
#
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# using as to give a module an alias. helps with readability. import
# module_name as mn
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# import all functions in a module with *. not recommended d/t name confusion
# from module_name import *
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



