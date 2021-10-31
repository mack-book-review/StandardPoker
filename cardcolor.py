import enum 

class CardColor(enum.Enum):
  blue1 = "blue1"
  blue2 = "blue2"
  blue3 = "blue3"
  blue4 = "blue4"
  blue5 = "blue5"

  red1 = "red1"
  red2 = "red2"
  red3 = "red3"
  red4 = "red4"
  red5 = "red4"

  green1 = "green1"
  green2 = "green2"
  green3 = "green3"
  green4 = "green4"
  green5 = "green5" 
 

  def __str__(self): 
    return self.value
   