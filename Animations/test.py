from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import sys
import random
import playsound

#speed = 1
Offset = 0
r = 7



def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)


'''def polarCircle(r, xc, yc):
    

    xPoints = []
    yPoints = []
    pi = math.pi

    
    for i in range(45):
        x = r * math.cos(pi/180*i)
        y = r * math.sin(pi/180*i)

        xPoints = xPoints + [x+xc, -x+xc, y + xc, -y+xc, -y+xc, y+xc, -x+xc, x+xc]
        yPoints = yPoints + [y+yc, -y+yc, x + yc, -x+yc, x+yc, -x+yc, y+yc, -y+yc]

    



    points = list(list())
    for i in range(len(xPoints)):
        points += [[xPoints[i], yPoints[i]]]

    return points
'''

def draw_circle(x, y):
    global Offset
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        if i < 90:
            glColor3f(1, 0, 0)
        elif i<180:
            glColor3f(0, 1, 0)
        elif i<270:
            glColor3f(0, 1, 1)
        elif i<360:
            glColor3f(1, 0, 0)
        
        glVertex2f(r * math.cos(Offset + math.pi * i / 180) + x, r * math.sin(Offset + math.pi * i / 180) + y)
    glEnd()



class Car:
    def __init__(self):
        
        self.speed = 1
        self.angle = float(input("Enter the angle of inclination: "))
        self.x1, self.y1 = -500, -500 * math.tan(math.radians(self.angle))
        self.x2, self.y2 = 500, 500 * math.tan(math.radians(self.angle))
        self.x = self.y = 0
        if self.angle > 0:
            self.to_right = False
        else:
            self.to_right = True
        self.start_point = [0, 0]


    def drawCar(self,x,y):
        
        if self.to_right:
            vertices = [[x, y + r],[x, y + 10 + r],[x + 10 , y + 10 + r],[x + 20 , y + 20 + r],[x + 40 , y + 20 + r],[x + 50 , y + 10 + r],[x + 60 , y + 10 + r],[x + 70 , y + r],]
        else:
            vertices = [[x, y + r],[x + 10, y + 10 + r],[x + 30 , y + 10 + r],[x + 30 , y + 20 + r],[x + 50 , y + 20 + r],[x + 60 , y + 10 + r],[x + 70 , y + 10 + r],[x + 70 , y + r],]

        rotated_vertices = self.get_rotated_points(vertices)

        tyres = [[x + 10, y + r],[x + 60, y + r],]

        rotated_tyres = self.get_rotated_points(tyres)

        glClear(GL_COLOR_BUFFER_BIT)

        glLineWidth(2.0)
        
        
        glBegin(GL_POLYGON)

        glColor3f(1,0,0)

        for vertex in rotated_vertices:
            glVertex2fv(vertex)
        
        glEnd()

        
        glBegin(GL_LINES)
        glColor3f(0,1,0)



        '''for tyre in rotated_tyres:
            draw_circle(tyre[0], tyre[1])'''

        glEnd()

        glutSwapBuffers()

    def buttons(self,key,x,y):
        global speed
        if key == b"d":
            self.to_right = True
        elif key == b"a":
            self.to_right = False
        elif key == b'f':
            self.speed += 3
        elif key == b's':
            self.speed -= 3
        elif key == b"h":
            playsound.playsound("./soundeffect.mp3", block=False)

    def update(self, value):
        global Offset
        x = self.start_point[0]
        y = self.start_point[1]
        if self.to_right:
            Offset -= 0.05 * self.speed
            x += self.speed * math.cos(math.radians(-self.angle))
            y += self.speed * math.sin(math.radians(-self.angle))
        else:
            Offset += 0.05 * self.speed
            x -= self.speed * math.cos(math.radians(-self.angle))
            y -= self.speed * math.sin(math.radians(-self.angle))
        if x > 500 :
            self.to_right = False
        elif x < -500:
            self.to_right = True
        self.start_point[0] = x
        self.start_point[1] = y
        glutPostRedisplay()
        glutTimerFunc(int(1000/60), self.update, 0)

    

def main():
    car = Car()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Animations")
    init()
    glutKeyboardFunc(car.buttons)
    glutDisplayFunc(car.drawCar)
    glutTimerFunc(0, car.update, 0)
    glutIdleFunc(car.drawCar)
    glutMainLoop()


main()