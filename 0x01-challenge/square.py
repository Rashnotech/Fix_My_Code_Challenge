#!/usr/bin/python3
""" a module that find the square """


class Square:
    """
    A class that perform geometry
    Args:
        width: width of the square
        height: height of the square
    """
    def __init__(self, *args, **kwargs):
        """ initialization """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Perimeter of the square """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Print the str version of square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
