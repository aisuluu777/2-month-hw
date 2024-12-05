class figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area (self):
        pass
    def info(self):
        pass

class square(figure):
    def __init__(self,side_length):
        super().__init__()
        self.__side_length = side_length


    def calculate_area(self):
        return self.__side_length ** 2


    def info (self):
        return f'square: side length: {self.__side_length}{self.unit}, area: {self.calculate_area()}{self.unit}'


class Rectangle(figure):
    def __init__(self,width,height):
        super().__init__()
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def info(self):
        return f'rectangle: width:{self.__width}{self.unit} height:{self.__height}{self.unit} area:{self.calculate_area()}{self.unit}'




square1 = square(5)
square2 = square(10)

rectangle1 = Rectangle(6,8)
rectangle2 = Rectangle(12,22)
rectangle3 = Rectangle(12,14)

figures = [square1,square2, rectangle1,rectangle2, rectangle3]

for char in figures:
    print(char.info())

