import time

import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame import DOUBLEBUF, OPENGL

radius = 0.2

slices = 10
stacks = 10


def drawTeapot(angle=0):
    position = (0, 0, 0)
    glPushMatrix()

    try:

        glTranslatef(*position)

        glRotatef(angle, 0, 0, 1)

        glutWireTeapot(.2)
        # glutWireTetrahedron()

        # glutWireCone(radius, height, slices, stacks)
        quadratic = gluNewQuadric()
        # gluCylinder(quadratic, 1, 1, height, slices, stacks)
        # glutSolidCylinder(radius, height, slices, stacks)

    finally:

        glPopMatrix()


def drawTetrahedron(angle=0):
    position = (0, 0, 0)
    glPushMatrix()

    try:

        glTranslatef(*position)

        glRotatef(angle, 0, 1, 0)

        # glutWireTeapot(.3)
        glutWireTetrahedron()

        # glutWireCone(radius, height, slices, stacks)
        quadratic = gluNewQuadric()
        # gluCylinder(quadratic, 1, 1, height, slices, stacks)
        # glutSolidCylinder(radius, height, slices, stacks)

    finally:

        glPopMatrix()


def displ1(swap=1, clear=1):
    if clear:
        glClearColor(0.0, 0.0, 0.0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    glutReshapeWindow(800, 800)

    x, y, width, height = glGetDoublev(GL_VIEWPORT)

    gluPerspective(

        30,

        width / float(height or 1),

        .25,

        200,

    )

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(

        0, 4, 1,

        0, 0, 0,

        0, 1, 0,

    )

    drawTeapot()
    drawTetrahedron()

    glutSwapBuffers()


def displ2(swap=1, clear=1):
    if clear:
        glClearColor(0.0, 0.0, 0.0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    glutReshapeWindow(800, 800)

    x, y, width, height = glGetDoublev(GL_VIEWPORT)

    gluPerspective(

        30,

        width / float(height or 1),

        .25,

        200,

    )

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(

        0, 4, 1,

        0, 0, 0,

        0, 1, 0,

    )
    teapotAngle = 30
    tetrahedronAngle = -45
    drawTeapot(teapotAngle)
    drawTetrahedron(tetrahedronAngle)

    glutSwapBuffers()


def displ3(clear=1):
    if clear:
        glClearColor(0.0, 0.0, 0.0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    glutReshapeWindow(800, 800)

    x, y, width, height = glGetDoublev(GL_VIEWPORT)

    gluPerspective(

        30,

        width / float(height or 1),

        .25,

        200,

    )

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(

        0, 4, 1,

        0, 0, 0,

        0, 1, 0,

    )
    position = (0, 0, 0)
    glPushMatrix()

    try:

        glRotatef(-140, 1.0, 0.0, 0.0)
        height = 0.6
        glTranslatef(0, 0.0, 0)
        glutWireCone(radius, height, slices, stacks)
        quadratic = gluNewQuadric()
        # gluCylinder(quadratic, 1, 1, height, slices, stacks)
        # glutSolidCylinder(radius, height, slices, stacks)

    finally:
        glPopMatrix()

    glPushMatrix()

    try:

        glRotatef(-140, 1.0, 0.0, 0.0)
        height = 0.6
        glTranslatef(-0.5, 0.0, 0)
        # glutWireCone(radius, height, slices, stacks)
        quadratic = gluNewQuadric()
        gluQuadricDrawStyle(quadratic, GLU_LINE)
        gluCylinder(quadratic, radius, 0.1, height, slices, stacks)
        # glutWireCylinder(radius, height, slices, stacks)
        # glutSolidCylinder(radius, height, slices, stacks)

    finally:
        glPopMatrix()

    glutSwapBuffers()


def displ4(clear=1):
    if clear:
        glClearColor(0.0, 0.0, 0.0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    glutReshapeWindow(800, 800)

    x, y, width, height = glGetDoublev(GL_VIEWPORT)

    gluPerspective(

        30,

        width / float(height or 1),

        .25,

        200,

    )

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(

        0, 4, 1,

        0, 0, 0,

        0, 1, 0,

    )
    position = (0, 0, 0)
    glPushMatrix()

    try:

        glRotatef(-270, 0.0, 1.0, 0.0)
        height = 0.6
        glTranslatef(0, 0.0, 0)
        glutWireCone(radius, height, slices, stacks)
        quadratic = gluNewQuadric()
        # gluCylinder(quadratic, 1, 1, height, slices, stacks)
        # glutSolidCylinder(radius, height, slices, stacks)

    finally:
        glPopMatrix()

    glPushMatrix()

    try:

        glRotatef(270, 1.0, 5.0, 0.0)
        height = 0.6
        glTranslatef(0, 0.0, 0)
        # glutWireCone(radius, height, slices, stacks)
        quadratic = gluNewQuadric()
        gluQuadricDrawStyle(quadratic, GLU_LINE)
        gluCylinder(quadratic, radius, 0.1, height, slices, stacks)
        # glutWireCylinder(radius, height, slices, stacks)
        # glutSolidCylinder(radius, height, slices, stacks)

    finally:
        glPopMatrix()

    glutSwapBuffers()


def idle():
    glutPostRedisplay()


starttime = time.time()


def key_pressed(*args):
    if args[0] == b'\033':
        sys.exit(0)


def firstTask():
    import sys

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutCreateWindow(b'First Task')

    glutDisplayFunc(displ1)

    glutKeyboardFunc(key_pressed)

    glutIdleFunc(displ1)

    glutMainLoop()


def secondTask():
    import sys

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutCreateWindow(b'Second Task')

    glutDisplayFunc(displ2)

    glutKeyboardFunc(key_pressed)

    glutIdleFunc(displ2)

    glutMainLoop()


def thirdTask():
    import sys

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutCreateWindow(b'Third Task')

    glutDisplayFunc(displ3)

    glutKeyboardFunc(key_pressed)

    glutIdleFunc(displ3)

    glutMainLoop()


def fourthTask():
    import sys

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutCreateWindow(b'Fourth Task')

    glutDisplayFunc(displ4)

    glutKeyboardFunc(key_pressed)

    glutIdleFunc(displ4)

    glutMainLoop()

def test_task(typeOfTask):
    if typeOfTask == "1":
        drawTeapot()
        drawTetrahedron()
    elif typeOfTask == "2":


        teapotAngle = 30
        tetrahedronAngle = -45

        drawTetrahedron(tetrahedronAngle)

def task(typeOfTask):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gluLookAt(

        0, 4, 1,

        0, 0, 0,

        0, 1, 0,

    )
    if typeOfTask == "1":
        drawTeapot()
        drawTetrahedron()
    elif typeOfTask == "2":
        glutDisplayFunc(displ2)

    if typeOfTask == "1":
        glutIdleFunc(displ1)
    elif typeOfTask == "2":
        glutIdleFunc(displ2)


def main():
    #firstTask()
    secondTask()
    #thirdTask()
    #fourthTask()


if __name__ == "__main__":
    main()
