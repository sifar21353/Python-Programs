def memo(func):
  memotize = {}

  def replace(x):
    if x not in memotize:
      memotize[x] = func(x)

    return memotize[x]

  return replace
