#9-1-2018

import math

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX()-p1.getX())+square(p2.getY()-p1.getY()))
    return dist
