from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin , cos , radians

sun_radius = 15
orbit_radius = 50
planet_radius = 10
planet_X=orbit_radius
planet_Y = 0
theta = 0
offset =0

def update(input):
	global theta
	global planet_X
	global planet_Y
	global offset
	offset +=1
	theta += 1
	planet_X = orbit_radius*cos(radians(theta))
	planet_Y = orbit_radius*sin(radians(theta))
	glutPostRedisplay()
	glutTimerFunc(int(1000/30),update,0)

	
def drawPlanet():
	global orbit_radius
	global planet_radius
	global planet_X
	global planet_Y
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(planet_X,planet_Y)
	for i in range(361):
		if i <= 180:
			glColor3f(1,0,0)
		elif i<= 360:
			glColor3f(0,0,1)
		glVertex2f(planet_radius*cos(radians(i+offset)) +planet_X, planet_radius*sin(radians(i+offset))+planet_Y)
	glEnd()
	glFlush()
		
	
	

def drawSun():
	global sun_radius
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(255,255,0)
	glVertex2f(0,0)
	for i in range(361):
		glVertex2f(sun_radius*cos(radians(i)) , sun_radius*sin(radians(i)))
	glEnd()
	glFlush()

def drawOrbit():
	global orbit_radius
	glColor3f(0,1,0)
	glBegin(GL_POINTS)
	for i in range(361):
		glVertex2f(orbit_radius*cos(radians(i)) , orbit_radius*sin(radians(i)))	
	glEnd()
	glFlush()
		
def drawScene():
	glClear(GL_COLOR_BUFFER_BIT)
	drawSun()
	drawOrbit()
	drawPlanet()
	
if __name__ == "__main__":
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB,GLUT_SINGLE)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	glutCreateWindow("Solar System")
	glutDisplayFunc(drawScene)
	glutTimerFunc(0,update,0)
	gluOrtho2D(-100,100,-100,100)
	glutMainLoop()
	
