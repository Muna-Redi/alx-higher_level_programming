#!/usr/bin/python3

"""
    defining class square that inherits from
    class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """" class square with Rectangle inheritance

        methods:

            __init__: decorator, which is same as class Rectangle

            area: gets the area of square

            display: displays the square

            update: updates the values of the square
    """

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
            public getter for the width attribute

            return: private instance attribute width
        """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for private instance attribute size

            Args:
               value (int): size of rectngle

            raises:
               TypeError: width must be an integer

               ValueError: width must be > 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be greater > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
            str method returns the string representation
            of the object/ class instance
        """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.height)

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
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]

        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.size = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """
           returns a dictionary representation of
            the class instance
        """

        return {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}
