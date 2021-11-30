from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import double


def init():
    """ function to Initialize screen """
    glClearColor(1.0, 1.0, 0.0, 1.0)  # clearing the screen and sets the color
    gluOrtho2D(-100.0, 100, -100, 100)  # sets the area to view


def hLine(xmin, xmax, y):
    """
    callback function to plot a horizontal line
    Args:
    xmin (float): x-cordinate of the starting point of the horizondal line.
    xmax (float): x-cordinate of the ending point of the horizondal line.
    ymax (float): y-cordinate which act as a offset of the horizondal line.
    Returns:
    None
    """
    glClear(GL_COLOR_BUFFER_BIT)  # clear the screen
    glPointSize(10.0)  # set the point size

    glBegin(GL_POINTS)  # start plotting points
    glColor3f(1, 0, 0)  # point color
    x = xmin
    while(x <= xmax):
        glVertex2f(x, y)  # this will plot the x,y points
        x = x + 0.05
    glEnd()
    glFlush()


def vLine(ymin, ymax, x):
    """Call back function to plot a vertical line
    Args:
    ymin (float): y-cordinate of the starting point of the vertical
    line.
    ymax (float): y-cordinate of the ending point of the vertical line.
    x (float): x-cordinate which act as a offset of the vertical line.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    y = ymin
    while(y <= ymax):
        glVertex2f(x, y)
        y = y + 0.5
    glEnd()
    glFlush()


def diagonalLine(x, y):
    """callback function to plot a diagonal line
    Args:
    x (float): x-cordinate of the starting point of the diagonal line.
    y (float): y-cordinate of the ending point of the diagonal line.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    while(x <= y):
        glVertex2f(x, x)

        x = x + 0.05
    glEnd()
    glFlush()


def main():
    choice = input("Enter Choice:1: Horizontal Line,2: Vertical Line,3: Diagonal Line")
    if(int(choice) == 1):
        xmin = float(input("Enter x start range: "))
        xmax = float(input("Enter x end range: "))
        y = float(input("Enter Y offset: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Plot Horizontal Line")
        glutDisplayFunc(lambda: hLine(xmin, xmax, y))
        init()
        glutMainLoop()
    elif (int(choice) == 2):
        ymin = float(input("Enter y start range: "))
        ymax = float(input("Enter y end range: "))
        x = float(input("Enter x offset: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Plot Vertical Line")
        glutDisplayFunc(lambda: vLine(ymin, ymax, x))
        init()
        glutMainLoop()
    elif (int(choice) == 3):
        x = float(input("Enter start cordinate(x,x) as x: "))
        y = float(input("Enter end cordinate(y,y) as y: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Plot diagonal Line")
        glutDisplayFunc(lambda: diagonalLine(x, y))

        init()
        glutMainLoop()
    else:
        print("Invalid choice")


main()
