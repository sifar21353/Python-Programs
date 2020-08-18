class Fraction():
  def __init__(self, n, d):
    self.numerator = n
    self.denominator = d

  def __add__(self, other):
    if self.denominator > other.denominator:
      large = self.denominator
      small = other.denominator
    else:
      large = other.denominator
      small = self.denominator
    index = large
    count = 2
    while True:
      if index % large == 0 and index % small == 0:
        break
      else:
        index = large * count 
        count = count + 1

    divide = index // self.denominator
    divide1 = index // other.denominator 

    self.numerator = self.numerator * divide
    other.numerator = other.numerator * divide1
    return (self.numerator + other.numerator,
    'over',
    int((other.denominator * divide1)))

  def __mul__(self, other):
    return (self.numerator * other.numerator,
    'over',
    self.denominator * other.denominator)

  def __lt__(self, other):
    if self.denominator > other.denominator:
      large = self.denominator
      small = other.denominator
    else:
      large = other.denominator
      small = self.denominator
    index = large
    count = 2
    while True:
      if index % large == 0 and index % small == 0:
        break
      else:
        index = large * count 
        count = count + 1

    divide = index // self.denominator
    divide1 = index // other.denominator 

    self.numerator = self.numerator * divide
    other.numerator = other.numerator * divide1

    if self.numerator > other.numerator:
      return '1'
    elif self.numerator < other.numerator:
      return '2'
    else:
      return '='

  def __sub__(self, other):
    if self.denominator > other.denominator:
      large = self.denominator
      small = other.denominator
    else:
      large = other.denominator
      small = self.denominator
    index = large
    count = 2
    while True:
      if index % large == 0 and index % small == 0:
        break
      else:
        index = large * count 
        count = count + 1

    divide = index // self.denominator
    divide1 = index // other.denominator 

    self.numerator = self.numerator * divide
    other.numerator = other.numerator * divide1
    return (self.numerator - other.numerator,
    'over',
    int((other.denominator * divide1)))
