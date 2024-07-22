import math

class Shape:
    def area(self):
         raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
     def __init__(self,length,width):
          self.length = length
          self.width = width

     def area(self):
          return self.length * self.width
     
class Circle(Shape):
     def __init__(self,radius** 2):
          self.radius = radius** 2

     def area(self):
          return 3.14159 * self.radius** 2    
     
          
