def plotaxes():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(0, -250)
    glVertex2f(0, 250)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(250, 0)
    glVertex2f(-250, 0)
    glEnd()


def plotgrid():
    glColor3f(0.202, 0.202, 0.202)
    for i in range(-250, 250, 50):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i, 250)
            glVertex2f(i, -250)
            glEnd()
            glBegin(GL_LINES)
            glVertex2f(250, i)
            glVertex2f(-250, i)
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


def plotTraingle(x1, x2, x3, y1, y2, y3):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()


def drawTranslated(x1, x2, x3, y1, y2, y3, tx, ty, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotaxes()
    plotgrid()

    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        newpoints.append([point[0]+tx, point[1]+ty])

    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2]
                 [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()


def drawScaled(x1, x2, x3, y1, y2, y3, tx, ty, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotaxes()
    plotgrid()

    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        newpoints.append([point[0]*tx, point[1]*ty])

    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2]
                 [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()


def drawScaledAboutPoint(x1, x2, x3, y1, y2, y3, tx, ty, px, py, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotaxes()
    plotgrid()

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


def drawReflected(x1, x2, x3, y1, y2, y3, ch, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotaxes()
    plotgrid()

    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        if(ch == 1):
            newpoints.append([point[0], -point[1]])
        elif(ch == 2):
            newpoints.append([-point[0], point[1]])
        elif(ch == 3):
            newpoints.append([-point[0], -point[1]])
        elif(ch == 4):
            newpoints.append([point[1], point[0]])
        elif(ch == 5):
            newpoints.append([-point[1], -point[0]])

    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2]
                 [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()


def drawReflectedAboutLine(x1, x2, x3, y1, y2, y3, a, b, c, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotaxes()
    plotgrid()
    plotLine(a, b, c, (1, 1, 1))

    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = [[x1, y1], [x2, y2], [x3, y3]]

    xToTranslate = -c/a
    thetaToRotate = math.atan(-a/b)

    # Translating such that the line crosses the origin
    for i, point in enumerate(newpoints):
        newpoints[i] = [point[0] - xToTranslate, point[1]]

    # Rotating such that the line coincides with x-axis
    for i, point in enumerate(points):
        newpoints[i] = rotate(point[0], point[1], -thetaToRotate)

    # Reflecting about x-axis
    for i, point in enumerate(points):
        newpoints[i] = [point[0], -point[1]]

    # Rotating back to original angle
    for i, point in enumerate(points):
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


def rotate(x, y, theta):
    return [round(x*math.cos(theta) - y*math.sin(theta)), round(x*math.sin(theta) + y*math.cos(theta))]


def drawRotated(x1, x2, x3, y1, y2, y3, theta, original_color=(0, 1, 0), transformed_color=(1, 0, 0)):
    plotaxes()
    plotgrid()

    points = [[x1, y1], [x2, y2], [x3, y3]]
    newpoints = []
    for point in points:
        newpoints.append(rotate(point[0], point[1], theta))

    glColor3f(original_color[0], original_color[1], original_color[2])
    plotTraingle(x1, x2, x3, y1, y2, y3)
    glColor3f(transformed_color[0], transformed_color[1], transformed_color[2])
    plotTraingle(newpoints[0][0], newpoints[1][0], newpoints[2]
                 [0], newpoints[0][1], newpoints[1][1], newpoints[2][1])
    glFlush()


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