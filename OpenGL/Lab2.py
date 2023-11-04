import numpy
import pygame as pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from pygame import DOUBLEBUF, OPENGL



SCENE_SCALE = -4
rotateAngle = 30

lightRotateAngle = 0
diffuseLight = [1, 1, 1, 1]
defaultSpecularLight = [0, 0, 0, 1]
coneSpecularLight = diffuseLight
#lightPos = [-10, 5, 5, 1]


radius = 1
height = 0.5
slices = 100
stacks = 100

def display_cone():
    glLoadIdentity()
    glPushMatrix()

    glTranslated(0.2, -0.5, SCENE_SCALE)
    glRotated(rotateAngle, 0, 1, 0)

    # rotate top up
    glRotated(180, 0, 1, 1)
    glColor3d(0.4961, 0, 0.3125)
    glMaterialfv(GL_FRONT, GL_SPECULAR, coneSpecularLight)
    glMateriali(GL_FRONT, GL_SHININESS, 30)
    glutSolidCone(0.5, 2, 50, 30)


    glMaterialfv(GL_FRONT, GL_SPECULAR, defaultSpecularLight)
    glPopMatrix()

SIZE = 1
SPHERE_RADIUS = 2

def display_tetrahedron():
    glLoadIdentity()
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glTranslated(0, 0, SCENE_SCALE)
    glRotated(30, 0, 1, 0)
    glColor4d(0.5, 0.156, 0.102, 0.6)
    glTranslated(-SIZE * .5, -(SPHERE_RADIUS - SIZE / 2) + 1.5, 0);
    glutSolidTetrahedron()

    glDisable(GL_BLEND)
    glPopMatrix()

def display_teapot():
    glLoadIdentity()
    glPushMatrix()
    texture = read_texture('/Users/george/PycharmProjects/OpenGL-test/inde.jpg')

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
    glTexGenf(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGenf(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)

    glTranslated(3, 0, SCENE_SCALE)
    glRotated(rotateAngle, 0, 1, 0)
    glColor3f(0.02, 0.72, 0.69)
    glTranslated(-SIZE * .5, -(SPHERE_RADIUS - SIZE / 2) + 1.5, -1);
    glutSolidTeapot(1.0)
    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

def read_texture(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    return textID

def main():
    import sys

    glutInit(sys.argv)
    pygame.init()
    width = 900
    height = 800
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glEnable(GL_LIGHT0)

    x = -10
    y = 5
    z = 5
    start_light_pos = [x, y, z, 1]

    red = 1.0
    green = 1.0
    blue = 1.0
    start_light_color = [red, green, blue, 1]
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(80.0, width / height, 1.0, 20.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
    glLightfv(GL_LIGHT0, GL_POSITION, start_light_pos)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y = y + 1
                if event.key == pygame.K_DOWN:
                    y = y - 1
                if event.key == pygame.K_LEFT:
                    x = x - 1
                if event.key == pygame.K_RIGHT:
                    x = x + 1
                if event.key == pygame.K_MINUS:
                    z = z - 1
                if event.key == pygame.K_EQUALS:
                    z = z + 1
                if event.key == pygame.K_r:
                    red = red + 0.1
                    lightZeroColor = [red, green, blue, 1.0]
                    if red + 0.1 >= 1:
                        red = 0
                    else:
                        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)

                if event.key == pygame.K_g:
                    green = green + 0.1
                    lightZeroColor = [red, green, blue, 1.0]
                    if green + 0.1 >= 1:
                        green = 0
                    else:
                        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)

                if event.key == pygame.K_b:
                    blue = blue + 0.1
                    lightZeroColor = [red, green, blue, 1.0]
                    if blue + 0.1 >= 1:
                        blue = 0
                    else:
                        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
                if event.key == pygame.K_f:
                    print(1)
                    x = start_light_pos[0]
                    y = start_light_pos[1]
                    z = start_light_pos[2]
                    glLightfv(GL_LIGHT0, GL_DIFFUSE, start_light_color)


        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        light_pos = [x, y, z, 1.]
        glLoadIdentity()
        glPushMatrix()

        glTranslated(0, 0, SCENE_SCALE)
        glRotated(rotateAngle, 0, 1, 0)

        glRotated(lightRotateAngle, 0, 1, 0)
        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

        glPopMatrix()
        display_cone()
        display_tetrahedron()
        display_teapot()
        print("x ", x, ", y", y, ", z", z)
        # glutSwapBuffers()
        pygame.display.flip()
        pygame.time.wait(10)


main()
