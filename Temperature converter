def temperature_convert(value, conversion_type): 
  def K2C():
    return value - 273.15
  def C2K():
    return value + 273.15

  if conversion_type == 'C2F':
    return (value * 9/5) + 32
  elif conversion_type == 'F2C':
    return (value - 32) * 5/9
  elif conversion_type == 'K2C':
    return K2C()
  elif conversion_type == 'C2K':
    return C2K()
  elif conversion_type == 'K2F':
    return (K2C(value) * 9/5) + 32
  else:
    return C2K((value - 32) * 5/9)
