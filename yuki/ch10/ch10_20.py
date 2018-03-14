#2018-2-20

#TODO: create cball.py function and read ch10.2

#2018-3-11
#p252
from math import pi,sin,cos,radians

def main():
    ang = eval(input("<<<TYPE>>> launch angle: "))
    vel = eval(input("<<<TYPE>>> initial velocity: "))
    h0 = eval(input("<<<TYPE>>> initial hight: "))
    time = eval(input("<<<TYPE>>> time interval between position calculation: "))

    theta=radians(ang)

    xpos=0
    ypos=h0
    xvel=vel*cos(theta)
    yvel=vel*sin(theta)

    while ypos>=0:
        xpos=xpos+time*xvel
        yvel1=yvel-time*9.8
        ypos=ypos+time*(yvel+yvel+1)/2.0
        yvel=yvel1

    print("\ndistance traveled: {0:0.1f} meters.".format(xpos))

main()
#print(radians(360))