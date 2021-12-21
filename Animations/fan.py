from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos , sin ,radians

offset = 10
def drawTriangle(x1,y1,x2,y2,x3,y3):
	glBegin(GL_TRIANGLES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glEnd()
	glFlush()

def update(input):
	global offset
	offset += .1
	glutPostRedisplay()
	glutTimerFunc(int(1000/30),update,0)

	
def rotate(x,y,angle):
	return x*(cos(radians(angle)))+y*(sin(radians(angle))) , -x*sin(radians(angle))+y*cos(radians(angle))
def plotPoints(x1 , y1 , side):
	glClear(GL_COLOR_BUFFER_BIT) 
	global offset
	x2 = x1-(side/2)
	y2 = y1+ (.866 * side)
	x3 = x1+side/2
	y3 = y1+ (.866 * side)
	x1 , y1 = rotate(x1,y1,offset)
	x2 , y2 = rotate(x2,y2,offset)
	x3 , y3 = rotate(x3,y3,offset)
	drawTriangle(x1,y1,x2,y2,x3,y3)
	x1 , y1 = rotate(x1,y1,120)
	x2 , y2 = rotate(x2,y2,120)
	x3 , y3 = rotate(x3,y3,120)
	drawTriangle(x1,y1,x2,y2,x3,y3)
	x1 , y1 = rotate(x1,y1,120)
	x2 , y2 = rotate(x2,y2,120)
	x3 , y3 = rotate(x3,y3,120)
	drawTriangle(x1,y1,x2,y2,x3,y3)

def plot(x,y,angle):
	glClear(GL_COLOR_BUFFER_BIT) 
	global offset
	x2 = x1-(side/2)
	y2 = y1+ (.866 * side)
	x3 = x1+side/2
	y3 = y1+ (.866 * side)
	glRotatef(offset,0,0,1)
	drawTriangle(x1,y1,x2,y2,x3,y3)
	glRotatef(120,0,0,1)
	drawTriangle(x1,y1,x2,y2,x3,y3)
	glRotatef(120,0,0,1)
	drawTriangle(x1,y1,x2,y2,x3,y3)
	


if __name__ == "__main__":
	x1 = int(input("x cordinate of the first point"))
	y1 = int(input("y cordinate of the seond point"))
	side = int(input("side of the triangel"))
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	glutCreateWindow("point plotting")
	glutDisplayFunc(lambda:plot(x1,y1,side))
	glutTimerFunc(0 , update, 0)
	gluOrtho2D(-100,100,-100,100)
	glutMainLoop()