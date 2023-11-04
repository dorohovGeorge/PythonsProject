import time

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

params_of_polished = [1, 1, 1, 1]

# Большой пузырь
Rs1 = 0.2
Gs1 = 0.2
Bs1 = 0.8
As1 = 0.3
sX1 = 4
sY1 = 5
sZ1 = 0
r1 = 5

# Средний пузырь
Rs2 = 0.8
Gs2 = 0.8
Bs2 = 0.2
As2 = 0.3
sX2 = 0
sY2 = -4
sZ2 = -2
r2 = 3

# Маленькия пузырь
Rs3 = 0.8
Gs3 = 0.2
Bs3 = 0.8
As3 = 0.3
sX3 = 8
sY3 = -7
sZ3 = -6
r3 = 2

# Цилиндр
Rc = 0.8
Gc = 0.2
Bc = 0.2
cX = -10
cY = -11
cZ = -7
rc = 0.5
hc = 15
Ac = 1

# Тор
Rt = 0.8
Gt = 0.2
Bt = 0.2
tX = -10
tY = 7
tZ = -7
srt = 0.5
lrt = 3


#cone
rcone1 = 0
height1 = 0
conex = 0
coney = -6.7
conez = 1

#cone2
rcone2 = 0
height2 = 0
cone2x = 0
cone2y = 6.7
cone2z = 1

def SoapBubbles():
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(Rs1, Gs1, Bs1, As1)
    glTranslatef(sX1, sY1, sZ1)
    glutSolidSphere(r1, 100, 100)
    glDisable(GL_BLEND)
    glPopMatrix()

    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(Rs2, Gs2, Bs2, As2)
    glTranslatef(sX2, sY2, sZ2)
    glutSolidSphere(r2, 100, 100)
    glDisable(GL_BLEND)
    glPopMatrix()

    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(Rs3, Gs3, Bs3, As3)
    glTranslatef(sX3, sY3, sZ3)
    glutSolidSphere(r3, 100, 100)
    glDisable(GL_BLEND)
    glPopMatrix()

    glPushMatrix()
    glColor4f(Rc, Gc, Bc, Ac)
    glTranslatef(cX, cY, cZ)
    glRotatef(-90, 1, 0, 0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #glutSolidCylinder(rc, hc, 100, 100)
    quadratic = gluNewQuadric()
    gluCylinder(quadratic, rc, rc, hc, 100, 100)
    glDisable(GL_BLEND)
    glPopMatrix()

    glPushMatrix()
    glColor3f(Rt, Gt, Bt)
    glTranslatef(tX, tY, tZ)
    glutSolidTorus(srt, lrt, 100, 100)
    glPopMatrix()
    #####
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(Rt, Gt, Bt, Ac)
    glTranslatef(conex, coney, conez)
    glRotatef(270, 1, 0, 0)
    glutSolidCone(rcone1, height1, 100, 100)
    glDisable(GL_BLEND)
    glPopMatrix()

    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(Rt, Gt, Bt, Ac)
    glTranslatef(cone2x, cone2y, cone2z)
    glRotatef(-270, 1, 0, 0)
    glutSolidCone(rcone2, height2, 100, 100)
    glDisable(GL_BLEND)
    glPopMatrix()


def main():
    global Rt, Gt, Bt, tX, tY, tZ, srt, lrt, Ac
    global Rc, Gc, Bc, cX, cY, cZ, rc, hc
    global As1, Gs1, Bs1, Rs1, sX1, sY1, sZ1, r1
    global Rs2, Gs2, Bs2, As2, sX2, sY2, sZ2, r2
    global Rs3, Gs3, Bs3, As3, sX3, sY3, sZ3, r3, rcone1, rcone2, height1, height2, conex, coney, cone2x, cone2y

    import sys
    glutInit(sys.argv)
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glEnable(GL_LIGHT0)
    x = 0
    y = 0
    z = 10
    start_light_pos = [x, y, z, 1]
    start_light_color = [1, 1, 1, 1]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, start_light_color)
    glLightfv(GL_LIGHT0, GL_POSITION, start_light_pos)

    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]), 0.1, 500.0)

    glTranslatef(0.0, 0.0, -20)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    count = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y = y + 1
                if event.key == pygame.K_s:
                    y = y - 1
                if event.key == pygame.K_a:
                    x = x - 1
                if event.key == pygame.K_d:
                    x = x + 1
                if event.key == pygame.K_z:
                    z = z - 1
                if event.key == pygame.K_x:
                    z = z + 1
                if event.key == pygame.K_r:
                    x = start_light_pos[0]
                    y = start_light_pos[1]
                    z = start_light_pos[2]
                    params_of_polished[0] = 1
                    params_of_polished[1] = 1
                    params_of_polished[2] = 1
                    glLightfv(GL_LIGHT0, GL_DIFFUSE, start_light_color)

        glClearColor(1.0, 1.0, 1.0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        light_pos = [x, y, z, 1.]

        glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
        SoapBubbles()

        if count <= 8:
            Rs1 = Rs1 + 0.08
            Gs1 = Gs1 + 0
            Bs1 = Bs1 - 0.2
            As1 = As1 + 0.2
            sX1 = sX1 - 0.5
            sY1 = sY1 - 0.125
            sZ1 = sZ1 + 0

            r1 = r1 - 0.375
            Rs2 = Rs2 - 0
            Gs2 = Gs2 - 0
            Bs2 = Bs2 - 0
            As2 = As2 + 0.2
            sX2 = sX2 - 0
            sY2 = sY2 + 0.5
            sZ2 = sZ2 + 0.25
            r2 = r2 - 0.125

            Rs3 = Rs3 - 0.75
            Gs3 = Gs3 + 0.075
            Bs3 = Bs3 - 0.75
            As3 = As3 + 0.2
            sX3 = sX3 - 1
            sY3 = sY3 + 0.375
            sZ3 = sZ3 + 0.75
            r3 = r3 - 0

            Rc = Rc - 0.0375
            Gc = Gc + 0.0375
            Bc = Bc + 0.0375
            cX = cX + 1.25
            cY = cY + 0.6
            cZ = cZ + 0.875
            rc = rc + 0.3
            hc = hc - 0.3
            Ac = Ac - 0.05

            Rt = Rt - 0.0375
            Gt = Gt + 0.0375
            Bt = Bt + 0.0375
            tX = tX + 1.25
            tY = tY + 0.4
            tZ = tZ + 0.7
            srt = srt - 0.0625
            lrt = lrt - 0.05

        if 8 < count < 16:
            #time.sleep(1)
            rcone1 = rcone1 + 0.4
            height1 = height1 + 0.5
            rcone2 = rcone2 + 0.4
            height2 = height2 + 0.5
            coney = coney - 0.25
            cone2y = cone2y + 0.25

        time.sleep(1)
        count = count + 1
        print("x ", x, ", y", y, ", z", z, " ", count)
        pygame.display.flip()
        pygame.time.wait(10)

main()
