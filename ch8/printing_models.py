# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: {}".format(current_design))
#     completed_models.append(current_design)
#
# print("The following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: {}".format(current_design))
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



# send instead a COPY of the list to the function like this:
# print_models(unprinted_designs[:], completed_models)

# function_name(list_name[:]) is a slice of the list, which is a copy of the
# list. This is a way to pass a copy of the list to the function, so that the
# original list is not modified.