# 2018 3 13

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours




def main():
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')
    best = makeStudent(infile.readline())
    for line in infile:
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())


if __name__ == '__main__':
    main()


from random import randrange
from util.graphics import GraphWin, Point
#from button import Button
#from dieview import DieView