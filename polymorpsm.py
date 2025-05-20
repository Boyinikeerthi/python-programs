#example on polymorphism
#parent class
class Shape:
    def area():
        print("Shape")
#child class
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("area=",self.side*self.side)
#child class
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area=",self.length*self.breadth)
shape=Shape()
Shape.area()
square=Square(10)
square.area()
rectangle=Rectangle(10,20)
rectangle.area()
              
