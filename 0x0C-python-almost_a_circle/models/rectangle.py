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

    def update(self, *args, **kwargs):
        """
            updates the attributes of the triangle with the
            supplied variable arguments and or keyword arguments.
            If args exists, kwargs is skipped

            Args:
                args: variable arguments representing id, widht
                height, x and y

            kwargs:
                keyword arguments which are dictionaries containing
                the the rectangle instance attribute name as key and
                value as its int value
        """
        if args is not None and len(args) != 0:
            for i in range(len(args)):

                if i == 0:
                    self.id = args[i]

                elif i == 1:
                    self.width = args[i]

                elif i == 2:
                    self.height = args[i]

                elif i == 3:
                    self.x = args[i]

                elif i == 4:
                    self.y = args[i]
        
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():

                    if key == "id":
                        self.id = value

                    elif key == "width":
                        self.width = value

                    elif key == "height":
                        self.height = value

                    elif key == "x":
                        self.x = value

                    elif key == "y":
                        self.y = value

    def display(self):
        """ displays the rectangle with the charrcter '#'"""

        for a in range(self.y):
            print()
        for i in range(self.height):

            for b in range(self.x):
                print(" ", end='')

            for j in range(self.width):
                print("#", end='')

            print()

    def __str__(self):
        """ overwrites the __str__ method with a string"""

        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(\
            self.__class__.__name__, self.id, self.x, self.y,\
                self.width, self.height)

    def to_dictionary(self):
        """ returns a dictionary representation of a class instance"""

        return {"x": self.x, "y": self.y, "id": self.id, "width": \
             self.width, "height": self.height}
