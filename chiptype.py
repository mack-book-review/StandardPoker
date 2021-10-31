import enum 

class ChipType(enum.Enum):
  White = 1
  Red = 5 
  Blue = 10
  Green = 25
  Black = 100


  def getImagePath(self,orientation=""):
    s = ""
    if orientation == "side":
      s = f"chip{self.chipType}White_sideBorder.png"
    else:
      s = f"chip{self.chipType}White_border.png"
    return s
  

  def __str__(self): 
    return f"Color: {self.name}, Dollar Value: ${self.color}"

  #overloaded operators
  def __ne__(self,other):
    return not (self == other)

  def __eq__(self,other):
    return self.name == other.name
  
  def __gt__(self,other):
    return self.value > other.value
  
  def __lt__(self,other):
    return self.value < other.value
  
  def __ge__(self,other):
    return self.value >= other.value
  
  def __le__(self,other):
    return self.value <= other.value

