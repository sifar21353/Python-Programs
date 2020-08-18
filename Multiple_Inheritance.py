class Polygon():
  pass

class Rectangle(Polygon):
  pass

class Parallelogram(Polygon):
  pass

class Square(Rectangle, Parallelogram):
  pass

print(Square.mro())
print(isinstance(Square(),Polygon))
print(isinstance(Square(),Rectangle))
print(isinstance(Square(),Parallelogram))
