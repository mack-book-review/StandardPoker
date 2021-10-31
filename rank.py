import enum 

class Rank(enum.Enum):
  Two = 2 
  Three = 3
  Four = 4 
  Five = 5 
  Six = 6 
  Seven = 7 
  Eight = 8
  Nine = 9 
  Ten = 10
  Jack = 11 
  Queen = 12 
  King = 13 
  Ace = 14

  def __str__(self): 
    if self.value >= 2 and self.value <= 10:
      return str(self.value)
    elif self.value == 11:
      return "J"
    elif self.value == 12:
      return "Q"
    elif self.value == 13:
      return "K"
    elif self.value == 14: 
      return "A"
      
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