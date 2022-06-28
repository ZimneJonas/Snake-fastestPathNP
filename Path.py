class Path:
  def __init__(self, leangth, width):
    self.grid = [[ll+ww*leangth for ww in range(width)] for ll in range(leangth)]


#TODO init with easy path like this:
# [16,15,14,13]
# [1,6,7,12]
# [2,5,8,11]
# [3,4,9,10]
aPath = Path(3,10)
print(aPath.grid)