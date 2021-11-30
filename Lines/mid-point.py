from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-50,50,-50,50)

def plotLine(x1,y1,x2,y2):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    x = x1
    y = y1

    glVertex2f(x, y) # plot the first point
    dx = x2 - x1
    dy = y2 - y1
    p = dy - (dx/2)
    while x < x2:
        x += 1
        if p < 0:
            p += dy
        else:
            y += 1
            p += dy - dx
            glVertex2f(x, y)

    glEnd()
    glFlush()
if __name__ == "__main__":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("PlotLine using Midpoint Algorithm")
    glutDisplayFunc(lambda: plotLine(x1,y1,x2,y2))
    init()
    glutMainLoop()