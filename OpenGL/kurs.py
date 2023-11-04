import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image as Image
import numpy
import time


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


def drawPlane():
    glBegin(GL_QUADS)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-3, -1.5, 2.1)
    glVertex3f(3., -1.5, 2.1)
    glVertex3f(3., -1.5, -11.)
    glVertex3f(-3., -1.5, -11.)

    glEnd()


def drawParallepiped():
    global texture

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glPushMatrix()
    glColor3f(0,1,0)
    glTranslatef(-1.5, -1.5, 0)
    glTranslatef(x, 0, 0)
    glTranslatef(0, -y, 0)
    glTranslatef(0, 0, z)

    glRotatef(-moveR, 0, 0, 1.0)

    # изменение размеров
    glScalef(0.3, 0.8, 0.3)
    glutSolidCube(2)
    glPopMatrix()

    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_TEXTURE_2D)


a = True
b = True
c = True


def draw():
    global moveR
    global goMove
    global x
    global y
    global z
    global a
    global b
    global c

    time.sleep(0.05)
    glClearColor(0, 0, 0, 0)
    glPushMatrix()
    glColor3f(0, 1, 1)
    glPopMatrix()

    glClearColor(0, 0, 0, 0)

    drawPlane()

    glPushMatrix()
    drawParallepiped()
    glPopMatrix()

    if (goMove):
        if moveR < 180:
            moveR += 1
            if -5 < moveR < 30:
                a = True
            elif 30 < moveR < 60:
                y += 0.002
                # time.sleep(0.1)
            elif 60 < moveR < 90:
                y += 0.004
                # time.sleep(0.2)
            # elif moveR == 90:
            #     time.sleep(5.2)
            elif 92 < moveR < 135:
                y -= 0.004
            elif 135 < moveR < 180:
                y -= 0.004
                z += 0.006
            print(x)

        if x < 1.47:
            x += 0.008


moveR = -5
goMove = False
x = 0
y = 0
z = 0


def main():
    global texture
    global goMove
    d_x = 1
    d_y = 1
    d_z = 10

    pygame.init()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInit(sys.argv)
    display = (1400, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    texture = read_texture('stich.jpg')



    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)


    glEnable(GL_LIGHTING)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 50)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 128)

    glEnable(GL_LIGHT0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(80., 1., 1., 80.)
    glTranslatef(-0.25, 0.14, -4.5)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    d_x -= 1
                    print('X coordinate = ', d_x)

                if event.key == pygame.K_d:
                    d_x += 1
                    print('X coordinate = ', d_x)

                if event.key == pygame.K_s:
                    d_y -= 1
                    print('Y coordinate = ', d_y)

                if event.key == pygame.K_w:
                    d_y += 1
                    print('Y coordinate = ', d_y)

                if event.key == pygame.K_q:
                    d_z -= 1
                    print('Z coordinate = ', d_z)

                if event.key == pygame.K_e:
                    d_z += 1
                    print('Z coordinate = ', d_x)

                if event.key == pygame.K_SPACE:
                    goMove = not goMove

        _ = pygame.key.get_pressed()
        glLightfv(GL_LIGHT0, GL_POSITION, [d_x, d_y, d_z, 1.0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
