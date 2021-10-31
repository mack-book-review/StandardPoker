import enum 

class Suit(enum.Enum):
  Clubs = 1
  Diamonds = 2 
  Hearts = 3
  Spades = 4


  #OVERLOAD COMPARISON OPERATORS
  def __gt__(self,other):
    return self.value > other.value 
  
  def __lt__(self,other):
    return self.value < other.value
  
  def __eq__(self,other):
    return self.value == other.value
  
  def __ne__(self,other):
    return self.value != other.value
  
  def __le__(self,other):
    return self.value <= other.value
  
  def __ge__(self,other):
    return self.value >= other.value