from chipentry import ChipEntry
from chiptype import ChipType

def test():


    ce1 = ChipEntry(ChipType.Blue,10)
    ce2 = ChipEntry(ChipType.Green,20)
    ce3 = ChipEntry(ChipType.Red,30)

    print(str(ce1.totalValue()))
    print(str(ce2.totalValue()))
    print(str(ce3.totalValue()))


if __name__ == "__main__":
    test()