import pytest

class Rectangle():

    def __init__(self, length, width):
        self.width = width
        self.length = length


    def permimeter(self):

        return ((self.width * 2)  + (self.length*2))


    def area(self):

        return (self.width * self.length )


    def __str__(self):
        return f"Rectangle of height {self.length} and width {self.width} has area of {self.area()} and perimeter of {self.permimeter()}"

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)

    # def area(self):
    #     return self.length * self.length
    #
    # def perimeter(self):
    #     return 4 * self.length
    def __str__(self):
        return  f" Square's area {super().area()}"


class  Cube(Square):

    def surface_area(self):
        face_area = super().area()
        return face_area *6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

 #r Multiple Inheritance and MRO ( Method Resoultion Order


class Triangle():

    def __init__(self , base, height):




if __name__ ==  "__main__":
    word ='Nayan'


    print(rec)
    sqr = Square(2)
    print(sqr ,sqr.area())
    cube=Cube(3)

