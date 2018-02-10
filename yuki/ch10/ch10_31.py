##YUKI_YAGI
##2018-2-10
# 267p
from math import pi, sin, cos, radians


class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self,time):
        self.xpos=+time*self.xvel
        yvel1=self.yvel-9.8*time
        self.ypos=self.ypos+time*(self.yvel+yvel1)/2.0
        self.yvel=yvel1

    def getY(self):
        return self.ypos
    #TODO:whyこれが必要？
    def getX(self):
        return self.xpos

def getInputs():
    a=eval(input("<<<TYPE>>> launchi angle (degree):"))
    v = eval(input("<<<TYPE>>> initial velocity (meters/sec):"))
    h = eval(input("<<<TYPE>>> initial height (meter):"))
    t = eval(input("<<<TYPE>>> time interval betweenposition calculations:"))
    return a,v,h,t




def main():
    angle, vel,h0,time=getInputs()
    cball=

main()

###
