def function_name(parameter_0, parameter_1='default value'):
    """Docstring"""
    print(parameter_0)
    print(parameter_1)


# no spaces around '=' in keyword args (in function calls) or default params

function_name(3, parameter_1='value')


# if params will exceed 79 char rule, put them on a new line, double indented

def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    """Docstring"""
    print(parameter_0)
    print(parameter_1)
    print(parameter_2)
    print(parameter_3)
    print(parameter_4)
    print(parameter_5)


