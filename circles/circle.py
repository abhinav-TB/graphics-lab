from OpenGL.GL import *
from OpenGL.GLU import *  # opengl utility library
from OpenGL.GLUT import *  # opengl utility toolkit
import sys
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # set background color
    # set the range of coordinate system
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)


def drawPixel(x, y):
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def midPointCircleDraw(xc, yc, r):
    x = r
    y = 0
    drawPixel(x+xc, y+yc)
    if (r > 0):
        drawPixel(x+xc, -y+yc)
        drawPixel(y+xc, x+yc)
        drawPixel(-y+xc, x+yc)
    P = 1 - r

    while x > y:
        y = y + 1
        if P <= 0:
            P = P + 2*y + 1

        else:
            x = x - 1
            P = P + 2*y - 2*x + 1
            
        drawPixel(x+xc, y+yc)
        drawPixel(-x+xc, y+yc)
        drawPixel(x+xc, -y+yc)
        drawPixel(-x+xc, -y+yc)
        drawPixel(y+xc, x+yc)
        drawPixel(-y+xc, x+yc)
        drawPixel(y+xc, -x+yc)
        drawPixel(-y+xc, -x+yc)


def non_polar_circle(xc, yc, radius):
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    x = xc - radius
    target = xc + radius
    glVertex2f(x, yc)
    glVertex2f(target, yc)
    factor = 7500
    incr = 1/factor
    x += incr
    while x < target:
        adder = math.sqrt(radius*radius - (x - xc)*(x - xc))
        glVertex2f(x, yc + adder)
        glVertex2f(x, yc - adder)
        x += incr
    glEnd()
    glFlush()


def polar_circle(xc, yc, radius):
    theta = 0
    factor = 500
    incr = 1 / factor
    target = math.pi / 4
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    while (theta <= target):
        x = radius*math.cos(theta)
        y = radius*math.sin(theta)
        glVertex2f(x + xc, y + yc)
        glVertex2f(-x + xc, -y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        glVertex2f(y + xc, x + yc)
        glVertex2f(-y + xc, -x + yc)
        glVertex2f(-y + xc, x + yc)
        glVertex2f(y + xc, -x + yc)
        theta = theta + incr
    glEnd()
    glFlush()
# push the pixels to display


def main():
    choice = input('''
	***MENU***
	Enter 1 to draw circle using mid point algorithm.
	Enter 2 to draw circle using non polar algorithm.
	Enter 3 to draw circle using polar algorithm.
	----------------------
	''')
    if int(choice) == 1:
        x = int(input("Enter the value of x center : "))
        y = int(input("Enter the value of y center : "))
        r = int(input("Enter the value of Radius: "))
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Plot Circle using Midpoint Circle Drawing Algorithm")
        glutDisplayFunc(lambda: midPointCircleDraw(x, y, r))
        init()
        glutMainLoop()
    elif int(choice) == 2:
        x = int(input("Enter the value of x center: "))
        y = int(input("Enter the value of y center: "))
        r = int(input("Enter the value of Radius: "))
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Plot Circle using Non Polar Circle")
        glutDisplayFunc(lambda: non_polar_circle(x, y, r))
        init()
        glutMainLoop()
    elif int(choice) == 3:
        x = int(input("Enter the value of x center: "))
        y = int(input("Enter the value of y center: "))
        r = int(input("Enter the value of Radius: "))
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Plot Circle using Polar Circle")
        glutDisplayFunc(lambda: polar_circle(x, y, r))
        init()
        glutMainLoop()
    else:
        print("Check your input and try again..")


main()