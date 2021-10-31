from chip import Chip 
from chiptype import ChipType
from chipentry import ChipEntry
import math
import functools

class Pot2(object):
  def __init__(self,chipEntries = []):
    self.chipEntries = chipEntries

  def addChipsOfType(self,chipType,number):
    index = self._getIndexForChipOfType(chipType)
    self.chipEntries[index].number += number

  def removeChipsOfType(self,chipType,number):
    index = self._getIndexForChipOfType(chipType)
    if self.chipEntries[index].number > 0:
      self.chipEntries[index].number += number

  def _getIndexForChipOfType(self,chipType):
    for i in len(range(self.chipEntries)):
      if self.chipEntries[i].chipType == chipType:
        return i

  def totalChipsOfType(self,chipType):
    return len(list(filter(lambda x: x.chipType == chipType,self.chipEntries)))

  def totalChips(self):
    return functools.reduce(lambda x,y: x.number + y.number, self.chipEntries)

  def totalValue(self):
    return functools.reduce(lambda x,y: x.totalValue() + y.totalValue(),self.chipEntries)

  def __eq__(self,other):
    return self.totalValue() == other.totalValue()

  def __add__(self,other):
    chipEntries = []
    for entry in self.chipEntries:
      for otherEntry in other.entries:
        if entry.chipType == otherEntry.chipType:
          chipEntries.append(ChipEntry(entry.chipType,entry.number + otherEntry.number))

    return Pot2(chipEntries)

  def __str__(self):
    str_list = [f"{entry.chipType.name} Chips: {entry.number}" for entry in self.chipEntries]
    s = "\n".join(str_list)
    s = f"Total Value: {self.totalValue()}\n{s}"
    return s

class Pot(object):

  def __init__(self,**kwargs):
    self.green_chips = 0 
    self.red_chips = 0 
    self.blue_chips = 0
    self.white_chips = 0 
    self.black_chips = 0

    if kwargs["green"]:
      self.green_chips += kwargs["green"]

    if kwargs["red"]:
      self.red_chips += kwargs["red"]  

    if kwargs["blue"]:
      self.red_chips += kwargs["blue"] 

    if kwargs["white"]:
      self.red_chips += kwargs["white"]

    if kwargs["black"]:
      self.red_chips += kwargs["black"]


    def removeChip(self,chipType,number):
      if(self._canRemove(chipType,number)):
        number = -math.abs(number)
        self._changeChipNumbers(chipType,number)

    
    def _canRemove(self,chipType,number):
      if chipType.name == "Green":
        return self.green_chips >= number
      
      if chipType.name == "Blue":
        return self.blue_chips >= number
      
      if chipType.name == "Red":
        return self.red_chips >= number
      
      if chipType.name == "White":
        return self.white_chips >= number
      
      if chipType.name == "Black":
        return self.black_chips >= number

      return False


    def addChip(self,chipType,number):
      number = math.abs(number)
      self._changeChipNumbers(chipType,number)

    def _changeChipNumbers(self,chipType,number):
      if chipType.name == "Green":
        self.green_chips += number
      
      if chipType.name == "Blue":
        self.blue_chips += number
      
      if chipType.name == "Red":
        self.red_chips += number
      
      if chipType.name == "White":
        self.white_chips += number
      
      if chipType.name == "Black":
        self.black_chips += number

    def totalValue(self):
      return self.red_chips*ChipType.Red.value + self.green_chips*ChipType.Green.value + self.blue_chips*ChipType.Blue.value + self.white_chips*ChipType.White.value + self.black_chips*ChipType.Black.value

    #str representation 
    def __str__(self):
      return f"White Chips: {self.white_chips}\nGreen Chips: {self.green_chips}\nRed Chips: {self.red_chips}\nBlue Chips: {self.blue_chips}\nBlack Chips:{self.blue_chips}\n Total Value:{self.totalValue()}"

    #overloaded operators
    def __eq__(self,other):
      return self.totalValue == other.totalValue
    
    def __ne__(self,other):
      return self.totalValue != other.totalValue

    def __gt__(self,other):
      return self.totalValue > other.totalValue

    def __lt__(self,other):
      return self.totalValue < other.totalValue

    def __ge__(self,other):
      return self.totalValue >= other.totalValue

    def __le__(self,other):
      return self.totalValue <= other.totalValue   