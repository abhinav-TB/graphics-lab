from glpy import *
import math

def plotTraingle(x1,x2,x3,y1,y2,y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()


def plotLine(a, b, c, color):
    x1 = -250
    y1 = -(a*x1 + c) / b
    x2 = 250
    y2 = -(a*x2 + c) / b
    glBegin(GL_LINES)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def rotate(x, y, theta):
    return [round(x*math.cos(theta) - y*math.sin(theta)), round(x*math.sin(theta) + y*math.cos(theta))]
@grid
def drawTranslated(x1,x2,x3,y1,y2,y3,tx,ty):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        newpoints.append([point[0]+tx,point[1]+ty])
    print(newpoints)

    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()

@grid
def drawRotated(x1,x2,x3,y1,y2,y3,theta):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        newpoints.append([(point[0]* math.cos(theta) - point[1] * math.sin(theta)), (point[0] * math.sin(theta) + point[1] * math.cos(theta))])
    print(newpoints)
    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()

@grid
def drawRotatedAroundPoint(x1, x2, x3, y1, y2, y3, px, py, theta, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotaxes()
    plotgrid()

    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        newpoints.append(rotate(point[0] - px, point[1] - py, theta))

    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0] + px, newpoints[1][0] + px, newpoints[2]
                 [0] + px, newpoints[0][1] + py, newpoints[1][1] + py, newpoints[2][1] + py)
    glFlush()

@grid
def drawScaled(x1,x2,x3,y1,y2,y3,tx,ty):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        newpoints.append([point[0]*tx,point[1]*ty])
    print(newpoints)
    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()

@grid
def drawScaledAboutPoint(x1, x2, x3, y1, y2, y3, tx, ty, px, py, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        newpoints.append([(point[0] - px)*tx, (point[1] - py)*ty])

    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0] + px, newpoints[1][0] + px, newpoints[2][0] +
                 px, newpoints[0][1] + py, newpoints[1][1] + py, newpoints[2][1] + py)
    glFlush()

@grid
def drawReflected(x1,x2,x3,y1,y2,y3,ch):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        if(ch==1):
            newpoints.append([point[0], -point[1]])
        elif(ch==2):
            newpoints.append([-point[0], point[1]])
        elif(ch==3):
            newpoints.append([-point[0], -point[1]])
        elif(ch==4):
            newpoints.append([point[1], point[0]])
        elif(ch==5):
            newpoints.append([-point[1], -point[0]])

        
    print(newpoints)
    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()
@grid
def drawReflectedAboutLine(x1, x2, x3, y1, y2, y3, a, b, c, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotLine(a, b, c, (1, 1, 1))

    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = [[x1, y1], [x2, y2], [x3, y3]]

    xToTranslate = -c/a if a!=0 else 0
    thetaToRotate = math.atan(-a/b) if not b==0 else math.pi/2

    # Translating such that the line crosses the origin
    for i, point in enumerate(newpoints):
        newpoints[i] = [point[0] - xToTranslate, point[1]]

    # Rotating such that the line coincides with x-axis
    for i, point in enumerate(newpoints):
        newpoints[i] = rotate(point[0], point[1], -thetaToRotate)

    # Reflecting about x-axis
    for i, point in enumerate(newpoints):
        newpoints[i] = [point[0], -point[1]]

    # Rotating back to original angle
    for i, point in enumerate(newpoints):
        newpoints[i] = rotate(point[0], point[1], thetaToRotate)

    # Translating back to origin position
    for i, point in enumerate(newpoints):
        newpoints[i] = [point[0] + xToTranslate, point[1]]

    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2]
                 [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()


if  __name__ == "__main__":
    app = glpy()
    print("\nEnter Triangle co-ordinates:")
    x1=float(input("\n\tx1: "))
    y1=float(input("\n\ty1: "))
    side=float(input("\n\tside: "))
    x2=x1+side
    y2=y1
    x3=x1+side/2
    y3=y1+0.86602540378*side

    print("\nChoose Transformations:\n\t1.Translation\n\t2.Rotation\n\t3.Scale\n\t4.Reflection\n\t5.Relflection about arbitary line\n\t6.Scale about a point \n\t7.Rotate around an arbitary point")
    ch=int(input("\nYour Choice: "))
    if ch == 1:
        tx=int(input("\nX translation: "))
        ty=int(input("\nY translation: "))
        app.run(lambda:drawTranslated(x1,x2,x3,y1,y2,y3,tx,ty))
    elif ch == 2:
        theta= (math.pi/180) * int(input("\nEnter Degress to be rotated: "))
        app.run(lambda:drawRotated(x1,x2,x3,y1,y2,y3,theta))
    elif ch == 3:
        tx=float(input("\nX scaling: "))
        ty=float(input("\nY scaling: "))
        app.run(lambda:drawScaled(x1,x2,x3,y1,y2,y3,tx,ty))
    elif ch == 4:
        ch=int(input("\nChoose Reflection:\n\t1.Reflection in X-axis\n\t2.Reflection in Y-axis\n\t3.Reflection in XY-axis\n\t4.Reflection in YX ,-X-axis\n\t5.Reflection in YX-axis"))
        app.run(lambda:drawReflected(x1,x2,x3,y1,y2,y3,ch))
    elif ch == 5:
        a=float(input("\nEnter a: "))
        b=float(input("\nEnter b: "))
        c=float(input("\nEnter c: "))
        app.run(lambda:drawReflectedAboutLine(x1,x2,x3,y1,y2,y3,a,b,c))
    elif ch == 6:
        tx=float(input("\nX scaling: "))
        ty=float(input("\nY scaling: "))
        px=float(input("\nX point: "))
        py=float(input("\nY point: "))
        app.run(lambda:drawScaledAboutPoint(x1,x2,x3,y1,y2,y3,tx,ty,px,py))
    elif ch == 7:
        theta= (math.pi/180) * int(input("\nEnter Degress to be rotated: "))
        px=float(input("\nX point: "))
        py=float(input("\nY point: "))
        app.run(lambda:drawRotatedAroundPoint(x1,x2,x3,y1,y2,y3,px,py,theta))

    else:
        print("\nInvalid Choice")


