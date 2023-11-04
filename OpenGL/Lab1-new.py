import time

import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame import DOUBLEBUF, OPENGL

radius = 0.2

slices = 7
stacks = 7


def draw_teapot(angle=0):
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(0.0, 0.0, -1.5)
    glRotatef(angle, 0, 0, 1)
    glScalef(0.7, 0.7, 0.7)
    glutWireTeapot(.14)
    glPopMatrix()


def draw_tetrahedron(angle):
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(0.0, 0.0, -1.5)
    glRotatef(angle, 0, 1, 0)
    glScalef(0.5, 0.5, 0.5)
    glutWireTetrahedron()
    glPopMatrix()


# def drawConeAndCylinder():
#     glLoadIdentity()
#
#     glPushMatrix()
#     glTranslatef(0., 0.0, -2)
#     glRotatef(80, 0.0, 1.0, 0.0)
#     height = 0.45
#     glutWireCone(radius, height, slices, stacks)
#     glPopMatrix()
#
#
#     glPushMatrix()
#     glTranslatef(-0.4, 0.0, -2)
#     glRotatef(-80, 0.0, 1.0, 0.0)
#     height = 0.45
#     # glutWireCone(radius, height, slices, stacks)
#     quadratic = gluNewQuadric()
#     gluQuadricDrawStyle(quadratic, GLU_LINE)
#     gluCylinder(quadratic, radius, 0.1, height, slices, stacks)
#     # glutWireCylinder(radius, height, slices, stacks)
#     # glutSolidCylinder(radius, height, slices, stacks)
#     glPopMatrix()

def draw_cone_and_cylinder_with_one_base(cone_angle=-90, cylinder_angle=-90, axis_x=1, axis_y=0, cone_trans=0.4,
                                         cylinder_trans=-0.4):
    glLoadIdentity()

    glPushMatrix()
    glTranslatef(cone_trans, 0.0, -2)
    glRotatef(cone_angle, axis_x, axis_y, 0.0)
    height = 0.45
    glutWireCone(radius, height, slices, stacks)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(cylinder_trans, 0.0, -2)
    glRotatef(cylinder_angle, axis_x, axis_y, 0.0)
    height = 0.45
    # glutWireCone(radius, height, slices, stacks)
    quadratic = gluNewQuadric()
    gluQuadricDrawStyle(quadratic, GLU_LINE)
    gluCylinder(quadratic, radius, 0.1, height, slices, stacks)
    # glutWireCylinder(radius, height, slices, stacks)
    # glutSolidCylinder(radius, height, slices, stacks)
    glPopMatrix()


def main():
    import sys
    glutInit(sys.argv)
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)


    gluPerspective(60, (display[0] / display[1]), 0.25, 50.0)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()


    typeOfTask = "1"
    tetAngle = 0
    teaAngle = 0
    tetrahedronAngle = -45
    teapotAngle = 30
    startConeAngle = -90
    startCylinderAngle = -90
    finishConeAngle = 80
    finishCylinderAngle = -80
    startAxisX = 1
    finalAxisX = 0
    startAxisY = 0
    finalAxisY = 1
    startConeTrans = 0.4
    startCylinderTrans = -0.4
    finishTrans = 0.0
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    glLoadIdentity()
                    typeOfTask = "1"
                if event.key == pygame.K_w:
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    glLoadIdentity()
                    typeOfTask = "2"
                if event.key == pygame.K_e:
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    glLoadIdentity()
                    typeOfTask = "3"
                if event.key == pygame.K_r:
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    glLoadIdentity()
                    typeOfTask = "4"

        if typeOfTask == "1":
            tetAngle = 0
            teaAngle = 0
        elif typeOfTask == "2":
            if tetAngle > tetrahedronAngle:
                tetAngle = tetAngle - 0.1
            if teaAngle < teapotAngle:
                teaAngle = teaAngle + 0.1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if typeOfTask == "1" or typeOfTask == "2":
            draw_tetrahedron(tetAngle)
            draw_teapot(teaAngle)

        if typeOfTask == "3":
            startConeAngle = -90
            startCylinderAngle = -90
            startAxisX = 1
            startAxisY = 0
            startConeTrans = 0.4
            startCylinderTrans = -0.4
            counter = 0
            draw_cone_and_cylinder_with_one_base(startConeAngle, startCylinderAngle, startAxisX, startAxisY)
        if typeOfTask == "4":
            if counter < 50:
                startAxisX = startAxisX - 0.02
            if counter < 50:
                startAxisY = startAxisY + 0.02
            if counter == 50:
                startAxisX = 0
                startAxisY = 1
            if startConeAngle < finishConeAngle and startAxisX == finalAxisX and startAxisY == finalAxisY:
                startConeAngle = startConeAngle + 1
            if startCylinderAngle < finishCylinderAngle and startAxisX == finalAxisX and startAxisY == finalAxisY:
                startCylinderAngle = startCylinderAngle + 1
            if startConeTrans > finishTrans and startCylinderAngle == finishCylinderAngle and startConeAngle == finishConeAngle:
                startConeTrans = startConeTrans - 0.01
            if startCylinderTrans < finishTrans and startCylinderAngle == finishCylinderAngle and startConeAngle == finishConeAngle:
                startCylinderTrans = startCylinderTrans + 0.01
            draw_cone_and_cylinder_with_one_base(startConeAngle, startCylinderAngle, startAxisX, startAxisY, startConeTrans,
                                                 startCylinderTrans)
            counter = counter + 1
        _ = pygame.key.get_pressed()
        pygame.display.flip()
        pygame.time.wait(10)

    # firstTask()
    # secondTask()
    # thirdTask()
    # fourthTask()


if __name__ == "__main__":
    main()
