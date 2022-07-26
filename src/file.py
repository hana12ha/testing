"""Example2"""


def addition(x: int, y: int) -> int:
    """Add x to y.


    Args:
        x: the input number
        y: the input number

    Returns:
        the addition of two numbers
    """


    add = x + y
    return add


print(addition(46,6))


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()


print(capital_case("hanane"))


