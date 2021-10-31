
class Chip(object):

  def __init__(self,chipType):
    self.chipType = chipType
    self.orientation = ""
  
  def getImagePath(self):
    s = ""
    if self.orientation == "side":
      s = f"chip{self.chipType}White_sideBorder.png"
    else:
      s = f"chip{self.chipType}White_border.png"
    return s

  def __gt__(self,other):
    return self.chipType > other.chipType
   
    
  def __lt__(self,other):
      return self.chipType < other.chipType
 

  def __ne__(self,other):
    return self.chipType != other.chipType
    
  def __eq__(self,other):
    return self.chipType == other.chipType

  def __ge__(self,other): 
    return self.chipType >= other.chipType
    
  def __le__(self,other):
    return self.chipType <= other.chipType

  def __str__(self):
    return str(self.chipType) + "(" + "Orientation: " + self.orientation + ")"