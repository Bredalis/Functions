
def decorator(function):
    """Decorates a function, showing a start and end message"""

    def inner_decorator(parameter_1, parameter_2):
        print("Start")
        function(parameter_1, parameter_2)
        print("End")

    return inner_decorator


@decorator
def power(base, exponent):
    """Prints the result of raising base to the exponent"""
    print(pow(base, exponent))


power(1, 8)
