from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi , cos  , sin , radians
import sys
from matplotlib.pyplot import get
import numpy as np
from playsound import playsound


# car settings

refPoint = [-200,-50]       # the bottom left point of the car
length = 100
height = 50
radius = length * 0.1
offset = 1
acceleration = 3

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)


def drawCircle(x,y):
    i = 0.0        
    glBegin(GL_TRIANGLE_FAN)    
    glVertex2f(x, y)
    for i in np.arange(0, 360.0, 1.0):
        if i < 180:
            glColor3f(0,0,1)
        else:
            glColor3f(1,0,0)
        glVertex2f(radius*cos(pi * (i+offset) / 180.0) + x, radius*sin(pi * (i+offset) / 180.0) + y)
    
    glEnd()

def create_line():
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glLineWidth(3)
        glBegin(GL_LINES)
        glVertex2f(-500, -60)
        glVertex2f(5000, -60)
        glEnd()

def drawCar():
    # Vertices of car body
    vertices = [
        [refPoint[0], refPoint[1]],
        [refPoint[0] , refPoint[1] + height * 0.40],
        [refPoint[0] + length*0.25, refPoint[1] + height],
        [refPoint[0] + length*0.75, refPoint[1] + height],
        [refPoint[0] + length, refPoint[1] + height * 0.40],
        [refPoint[0] + length, refPoint[1]]
    ]

    # Centres of car tyres
    tyres = [
        [refPoint[0] + length * 0.25, refPoint[1]],
        [refPoint[0] + length * 0.75, refPoint[1]]
    ]
    
    # vertices = get_rotated_points(vertices)
    # tyres = get_rotated_points(tyres)
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2.0)
    
    create_line()
    # Car body
    glBegin(GL_POLYGON)

    glColor3f(30, 0, 200)

    for i in vertices:
        glVertex2fv(i)

    glEnd()

    drawCircle(refPoint[0] + length * 0.20, refPoint[1])
    drawCircle(refPoint[0] + length * 0.80, refPoint[1])

    glutSwapBuffers()

def update(input):
    global acceleration
    global offset
    glutPostRedisplay()
    refPoint[0] += acceleration
    offset -= 5 if acceleration > 0 else -5
    glutTimerFunc(40, update, 0)


def changeDirection():
    global acceleration
    global offset
    acceleration = acceleration * -1



def keyPressed(key, x, y):
    global acceleration
    if key == b'w':
        acceleration += 2
    
    if key == b's':
        acceleration -= 2
    if key == b'a' or key == b'd':
        changeDirection()
    
    if key == b'h':
        playsound('car.wav')
    

     
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Animations")
    init()
    glutKeyboardFunc(keyPressed)
    glutTimerFunc(0, update, 0)
    glutIdleFunc(drawCar)
    glutMainLoop()

main()