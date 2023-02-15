#TODO
# Create a base class Polygon with basic features and properties like no of sides , write init and str
#  dunders to initialize and print info on the object
#  define methods like area, volume, perimeter etc
#  Inherit the base class to create like SOAURE, RECTANGLE, QUADILETRAL, PENTAGON HEXAGON etc
#  with respective properties and methods.


#code for the instructions
from math import sqrt

#base class
class Polygon : 
    def __init__(self, n : int) :
        #n is the number of sides (sq = 4 , re = 4 , pent = 5) and so forth
        self.n = n 
        print('')
        print('Basic properties:')
        if(self.n == 4):
            print(f"It consists of {self.n} sides which can be a square/rectangle/quadrilateral")
        if(self.n == 5):
            print(f"It consists of {self.n} sides which is pentagon")
        if(self.n == 6):
            print(f"It consists of {self.n} sides which is Hexagon")

    #method for finding Area
    def Area(self ,l :int , b=0 ):
        if(b == 0):
            return l * l
        return l * b
    
    #method for finding Perimiter
    def Perimeter(self , l:int  , b =0):
        if(b == 0):
            return self.n * l
        
        return 2 *(l + b)
    
    def Volume(self , l:int , b=0 , h=0):
        if(b == 0 and h ==0):
            return l * l* l 
        return l * b * h
    
    
#inherited from polygon
class Square(Polygon):
    #area and perimeter finding methods are inherited from base class
    pass

#inherited from polygon
class Rectangle(Polygon):
    #area and perimter finding methods are inherited from base class
    pass


#inherited from polygon
class Pentagon(Polygon):
    #method for finding area of Pentagon since formula is different
    def Area(self , a):
        area = (sqrt(5 * (5 + 2 *(sqrt(5)))) * a * a) / 4
        return area


#inherited from polygon
class Quadrilateral(Polygon):
    # area of quadrilateral is base * height (and is overided from base class))
    def Area(self,  b:int , h :int):
        return b * h
    
    # perimeter of quad is sum of all sides (and is overided from base class)
    def Perimeter(self, a:int ,b:int,c:int,d:int):
        return a + b + c + d 

#inherited from polygon
class Hexagon(Polygon):
    #method for finding area of Hexagon since formula is different (and is overided from base class)
    def Area(self , a :int):
        return ((3 * sqrt(3) *(a * a)) / 2)


#all the instances/object of inherited class
sq = Square(4)
print(f"The area of square is: {sq.Area(4)}")
print(f"The perimeter of square is: {sq.Perimeter(4)}")

re = Rectangle(4)
print(f'The area of rectangle is: {re.Area(5,9)}')
print(f'The perimeter of rectangle is: {re.Perimeter(5,9)}')

pe = Pentagon(5)
print(f"The area of Pentagon is : {pe.Area(10)}")
print(f"The Perimeter of pentagon is : {pe.Perimeter(10)}")

qu = Quadrilateral(4)
print(f"The area of Quadrilateral is : {qu.Area(12 ,16)}")
print(f"The area of Quadrilateral is : {qu.Perimeter(12,13,14,15)}")

he= Hexagon(6)
print(f"The Area of Hexagon is :{he.Area(12)}")
print(f"The perimeter of Hexagon is :{he.Perimeter(13)}")