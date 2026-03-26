class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printPoint(self):
        print("(", self.x, ",", self.y, ")", end="")


class LineSegment:
    
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2:
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            x1, y1, x2, y2 = args
            self.__d1 = Point(x1, y1)
            self.__d2 = Point(x2, y2)
        elif len(args) == 1:
            S = args[0]
            self.__d1 = Point(S.__d1.x, S.__d1.y)
            self.__d2 = Point(S.__d2.x, S.__d2.y)
    def printLine(self):
        print("d1 = ", end="")
        self.__d1.printPoint()
        print(" , d2 = ", end="")
        self.__d2.printPoint()
        print()

print("Mac dinh:")
l1 = LineSegment()
l1.printLine()

print("Truyen 2 point:")
p1 = Point(2, 3)
p2 = Point(5, 6)
l2 = LineSegment(p1, p2)
l2.printLine()

print("Truyen 4 so:")
l3 = LineSegment(1, 2, 3, 4)
l3.printLine()
print("Copy:")
l4 = LineSegment(l3)
l4.printLine()
