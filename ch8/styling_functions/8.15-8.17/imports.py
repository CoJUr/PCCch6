# import make_pizzas
#
# make_pizzas.make_pizza(16, 'pepperoni')


# from make_pizzas import make_pizza
#
# make_pizza(16, 'pepperoni')


# from make_pizzas import make_pizza as mp
#
# mp(16, 'pepperoni', 'peppers', 'onions', 'sausage')


# import make_pizzas as mp
#
# mp.make_pizza(13, 'pepperoncinis', 'pineapple', 'ham', 'sausage')


# from make_pizzas import *
#
# make_pizza(14, 'turkey', 'bacon', 'avocado', 'tomato', 'onion', 'spinach')

# best approach: import the entire module and use the dot notation to access
# the functions you need. this approach is also the most efficient in terms of
# memory usage. else, import the specific functions you need

import make_pizzas

make_pizzas.make_pizza(17, 'chicken', 'bbq sauce', 'onion', 'mushroom',
                       'spinach')



