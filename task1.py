class Rectangle:

    def __init__(self, length=1.0, width=1.0):
        self.__length = length
        self.__width = width

    def __str__(self):
        return f"{self.__width} x {self.__length}"

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value: float):
        if not isinstance(value, float):
            raise TypeError('Value must be a floating-point')
        if 0.0 < value < 20.0:
            self.__length = value
        else:
            raise ValueError("The value must be a floating-point larger than 0.0 and less than 20.0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: float):
        if not isinstance(value, float):
            raise TypeError('Value must be a floating-point')
        if 0.0 < value < 20.0:
            self.__width = value
        else:
            raise ValueError("The value must be a floating-point larger than 0.0 and less than 20.0")


if __name__ == '__main__':
    rectangle = Rectangle(1.0, 3.0)
    print(rectangle.perimeter())
    print(rectangle.area())
    rectangle.length = 2.0
    rectangle.width = 2.0
    print(rectangle.perimeter())
    print(rectangle.area())
