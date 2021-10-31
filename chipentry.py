from chiptype import ChipType

class ChipEntry(object):

    def __init__(self,chipType,number):
        self.chipType = chipType
        self.number = number

    def totalValue(self):
        return self.chipType.value*self.number

    def __str__(self):
        return f"{self.chipType.name} Chips: {self.number}"

    def __eq__(self, other):
        return self.chipType == other.chipType and self.number == other.number