#!/usr/bin/python3

""" Defining class Rectngle that inherits from class Base

    methods:
        __init__: class decorator
"""


from models.base import Base

class Rectangle(Base):
    """ class Rectangle

        Attributes:

            private instance attributes:
                width (int): width of rectngle
                height (int): height of rectangle
                x (int): private instance attrinute
                y (int): private instance attribute

        methods:
            __init__: class decorator

            area: returns the area of the rectangle

        getter:
            width (int): gets the width of an instance
            height (int): gets the height attribute of an instance
            x (int): gets gets the attribute x of an instance
            y (int): gets the attribute y of an instance

        setter:
            width (int): sets the width of an instance
            height (int): sets the height attribute of an instance
            x (int): sets private instance attribute x
            y (int): sets private instance attribute y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class decorator

            Args:
                width: width of the triangle
                height (int): height of rectangle
                x (int): private instance attrinute
                y (int): private instance attribute
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            public getter for the width attribute

            return: private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter for private instance attribute width

            Args:
               width (int): width of rectngle

            raises:
               TypeError: width must be an integer

               ValueError: width must be > 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be greater > 0")

        self.__width = width

    @property
    def height(self):
        """
            public getter for the height attribute

            return: private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter for private instance attribute height

            Args:
               height (int): height of rectngle

            raises:
               TypeError: height must be an integer

               ValueError: height must be > 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be greater > 0")

        self.__height = height

    @property
    def x(self):
        """ 
            public getter for the attribute x

            return: private instance attribute x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ 
            setter for private instance attribute x

            Args:
               x (int): x value of rectngle

            raises:
               TypeError: x must be an integer

               ValueError: x must be >= 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be greater >= 0")

        self.__x = x

    @property
    def y(self):
        """
            public getter for the attribute y

            return: private instance attribute y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter for private instance attribute y

            Args:
               y (int): y value of rectngle

            raises:
               TypeError: y must be an integer

               ValueError: y must be >= 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be greater >= 0")

        self.__y = y

    def area(self):
        """ computes the area of the rectangle

            return: the area of the rectangle
        """

        return (self.width * self.height)

    def display(self):
        """ displays the rectangle with the charrcter '#'"""

        for i in range(self.height):

            for j in range(self.width) :
                print("#", end='')

            print()

    def __str__(self):
        """ overwrites the __str__ method with a string"""

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,\
         self.x, self.y, self.width, self.height)
