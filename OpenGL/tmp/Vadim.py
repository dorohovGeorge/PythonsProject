from time import sleep

import pygame

from Cube import *
from Moving_cube import *
import numpy

# http://openglsamples.sourceforge.net/cube2_py.html

R = 1
l_pos_x = 1  # light source shift value on X
l_pos_y = 2  # light source shift value on Y
p_pos_x = 0  # polygon shift value on X
withSource = True

SURFACE_WIDTH = 30
SURFACE = [(-SURFACE_WIDTH, -0.5, -SURFACE_WIDTH),
           (SURFACE_WIDTH, -0.5, -SURFACE_WIDTH),
           (SURFACE_WIDTH, -0.5, SURFACE_WIDTH),
           (-SURFACE_WIDTH, -0.5, SURFACE_WIDTH)]

global cube
global not_convex
global texid


def InitGL(Width, Height):
    global ambient
    global dAmbient
    global withSource
    global texid
    global cube
    global not_convex
    bind()
    cube = Cube(texid)
    not_convex = NotConvex(texid)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    # light
    # glLightModelfv(GL_LIGHT_MODEL_COLOR_CONTROL,GL_SINGLE_COLOR)
    # glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, WHITE)  # lighting model
    glEnable(GL_LIGHTING)  # lighting on
    glEnable(GL_NORMALIZE)
    lighting(withSource)

    draw()


def lighting(with_source=False):
    light_pos = (l_pos_x, l_pos_y, 4)
    # light source
    if with_source:
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, WHITE)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, WHITE)
        glTranslate(light_pos[0], light_pos[1], light_pos[2])
        #
        glutSolidSphere(0.1, 30, 30)
        # undo changes
        glTranslate(-light_pos[0], -light_pos[1], -light_pos[2])
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0, 0, 0, 0))
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))
    # light
    # glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, 90)
    # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (1,0,0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, WHITE)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glEnable(GL_LIGHT0)


def special_keys(key, x, y):
    global p_pos_x, t
    global p_pos_y
    if key == GLUT_KEY_LEFT:
        p_pos_x -= 0.1
        t = -0.05
    if key == GLUT_KEY_RIGHT:
        p_pos_x += 0.1
        t = +0.05
    not_convex.position(t)
    glutPostRedisplay()


def keys(key, x, y):
    global withSource
    global tmp
    global l_pos_x
    global l_pos_y

    if ord(key) == ord("w"):  # Клавиша вверх
        l_pos_y += 0.2  # Уменьшаем угол вращения по оси Х
    if ord(key) == ord("s"):  # Клавиша вниз
        l_pos_y -= 0.2  # Увеличиваем угол вращения по оси Х
    if ord(key) == ord("a"):  # Клавиша влево
        l_pos_x -= 0.2  # Уменьшаем угол вращения по оси Y
    if ord(key) == ord("d"):  # Клавиша вправо
        l_pos_x += 0.2  # Увеличиваем угол вращения по оси Y
    if ord(key) == ord("q"):
        withSource = not withSource
        print("Source")

    glutPostRedisplay()


def surface():
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, GREEN)
    glBegin(GL_QUADS)
    for vertex in SURFACE:
        D = SURFACE_WIDTH * 2
        glNormal3f(vertex[0] / D, vertex[1] / D, vertex[2] / D)
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0) # (0.0, 0.0, -6.0)
    gluLookAt(0.0, 0.0, 0.0,
              -0.2, -0.4, -1,
              0.0, 1.5, 0.0)
    """(0.0, 0.0, 0.0,
              -0.2, -0.4, -1,
              0.0, 1.5, 0.0)"""
    surface()
    glPushMatrix()
    cube.draw()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glPushMatrix()
    not_convex.draw()
    glPopMatrix()
    lighting()
    glutSwapBuffers()


def load(file_name):
    """textureSurface = Image.open(file_name)
    textureSurface = textureSurface.convert("RGBA").rotate(180)
    textureData = numpy.array(list(textureSurface.getdata()), numpy.int8)"""

    textureSurface = pygame.image.load(file_name)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def bind():
    global texid
    global qobj
    global qob
    texid = []
    for i in range(1, 3):
        texid.append(load('{}.jpg'.format(i)))
    qobj = gluNewQuadric()
    qob = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    gluQuadricTexture(qob, GL_TRUE)
    return texid


def idle():
    t = numpy.pi / 20 - 0.006 * (not_convex.unit * not_convex.rotation_limit + not_convex.rotation_times)

    not_convex.position(t)
    glutPostRedisplay()


def mouse(*args):
    global xrot, yrot
    global xdiff, ydiff
    global mouseDown
    if (args[0] == GLUT_LEFT_BUTTON and args[1] == GLUT_DOWN):
        mouseDown = True
        sleep(1)
    else:
        mouseDown = False


def main():
    window_size = [700, 700]
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(*window_size)
    glutInitWindowPosition(250, 100)
    glutCreateWindow("kek")
    InitGL(700, 700)

    glutIdleFunc(idle)
    glutDisplayFunc(draw)
    glutSpecialFunc(special_keys)
    glutKeyboardFunc(keys)
    glutMouseFunc(mouse)

    glutMainLoop()


if __name__ == "__main__":
    main()
