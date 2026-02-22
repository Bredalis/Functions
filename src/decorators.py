
def decorator(function):
    """Decorates a function, showing a start and end message"""
    def inner_decorator():
        print("Start")
        function()
        print("End")

    return inner_decorator


@decorator
def addition():
    """Prints the result of the addition 1 + 2"""
    print(1 + 2)


addition()
