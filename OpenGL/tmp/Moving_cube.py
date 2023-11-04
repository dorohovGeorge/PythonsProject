from time import sleep

from OpenGL.GL import *
from constants import *
from PIL import Image
import numpy
from Cube import CUBE_WIDTH
from Fall import *

W = 0.1 # 0.085
N = 4
fall_direction = Fall(v0=10) #10

V = [[-2*W, +2*W, +2*W],  # 0
     [-2*W, +2*W, -2*W],  # 1
     [+W, +W, -W],  # 2
     [+W, +W, +W],  # 3
     [0, 0, 0],  # 4
     [-W, -W, +W],  # 5
     [-W, -W, -W],  # 6
     [+W, -W, -W],  # 7
     [+W, -W, +W]]  # 8

T_PLANES = [
    (V[0], V[1], V[4]),
    (V[1], V[6], V[4]),
    (V[6], V[5], V[4]),
    (V[5], V[0], V[4]),
    #
    (V[3], V[2], V[4]),
    (V[2], V[7], V[4]),
    (V[7], V[8], V[4]),
    (V[8], V[3], V[4]),
    #
    #
    (V[0], V[1], V[4]),
    (V[1], V[2], V[4]),
    (V[2], V[3], V[4]),
    (V[3], V[0], V[4]),
    #
    (V[7], V[8], V[4]),
    (V[6], V[7], V[4]),
    (V[5], V[6], V[4]),
    (V[8], V[5], V[4])
]
for i in V:  # перемещение куба наверх
    # i[0] -= CUBE_WIDTH
    i[1] += 2 * CUBE_WIDTH
    i[2] += CUBE_WIDTH + CUBE_WIDTH + 10


class NotConvex:

    def __init__(self, texid):
        self.t = 0.0
        self.is_rotated = False
        self.rotation_times = 0
        self.fall_t = 0
        self.change_direction_times = 0
        self.unit = 1
        self.update(self.unit)
        self.rotation_limit = N
        self.current_x = 0.0
        self.current_z = 0.0
        self.angle_x = 0.0
        self.angle_z = 0.0
        self.fall_counter = 0
        self.incline_angle = 0
        self.incline_shift = 0
        self.update(self.unit)
        self.surface_motion = 0
        self.surface_angle = 0
        self.x_shift = 0
        self.texture_id = texid

    def draw(self):
        # print(self.rotation_times)
        if not self.is_rotated:
            if self.unit == 1 and self.rotation_times > self.rotation_limit:  # куб идет, меняем направление
                self.change_direction()
                # if self.rotation_times > 1:
                #     print("here we go")

            self.rotate(self.unit)
        else:
            self.update(self.unit)

        if self.unit == 3:  # куб начинает падать
            if self.incline_angle > -45:
                glTranslatef(0.02, 0, 0)  # -0.55
                glTranslatef(0.0, self.incline_shift, 0.0)
                self.rotate_about_center(self.incline_angle, 0.0, 0.0, 1.0)
                self.incline_angle -= 0.5
                self.incline_shift -= 0.001
                # sleep(0.001)
            else:
                self.unit = 2

        if self.unit == 2:  # куб падает с куба
            if self.fall_counter != 0 or self.fall_counter != 1:
                glTranslatef(0.9, 0, 0) # (0.7, 0, 0)
                glTranslatef(0.0, self.incline_shift, 0.0)
                self.rotate_about_center(self.incline_angle, 0.0, 0.0, 1.0)
                #
                if self.fall_counter > 100:
                    self.unit = 4
                else:
                    if self.angle_z > -30:
                        self.angle_z -= 1
                    self.rotate_about_center(self.angle_z, 0, 0, 1.0)

                self.update(self.unit)

            self.fall_counter += 1
            print(self.fall_counter)
            sleep(0.001)

        if self.unit == 4:
            if self.surface_angle != 0 or self.surface_angle != -0.5 or self.surface_angle != -1.0:
                glTranslatef(0.7 + self.x_shift, -0.6, 0)
                glTranslatef(0.2, self.incline_shift, 0.0) # (0.0, self.incline_shift, 0.0)
                self.rotate_about_center(self.angle_z + self.incline_angle + self.surface_angle, 0.0, 0.0, 1.0)
                # sleep(100)
                print(self.angle_z + self.incline_angle + self.surface_angle)
            if self.angle_z + self.incline_angle + self.surface_angle > -90:
                self.surface_angle -= 0.5
            print(self.angle_z + self.incline_angle + self.surface_angle)
            # if (self.angle_z + self.incline_angle + self.surface_angle <= 0):#95
            #     self.surface_angle -= 0.05
            # glTranslatef(-1 * (self.rotation_limit + 3.8) * W, 0, 0)  # -0.55
            # self.rotate_about_center(self.incline_angle, 0.0, 0.0, 1.0)
            # self.rotate_about_center(self.angle_z, 0, 0, 1.0)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, GL_RED)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id[0])
        glBegin(GL_TRIANGLES)
        for plane in T_PLANES:
            for vertex in plane:
                normale_x = vertex[0] - V[4][0]
                normale_y = vertex[1] - V[4][1]
                normale_z = vertex[2] - V[4][2]
                glNormal3f(normale_x, normale_y, normale_z)
                glTexCoord2f(vertex[0], vertex[1])
                glTexCoord2f(vertex[2], vertex[1])
                glTexCoord2f(vertex[0], vertex[2])
                glVertex3f(vertex[0], vertex[1], vertex[2])
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0, 0, 0, 0))

    def position(self, t=0):
        self.t = t

    def read_texture(self, filename):
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
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0,
                     GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return textID

    def rotate_about_center(self, angle, x, y, z):
        glTranslatef(V[4][0], V[4][1], V[4][2])
        glRotatef(angle, x, y, z)
        glTranslatef(-V[4][0], -V[4][1], -V[4][2])

    def change_direction(self):
        self.change_direction_times += 1
        # self.rotation_times = 1
        self.is_rotated = False
        self.unit = 3

    def rotate(self, unit):
        if unit == 1:
            self.rotateXY2()

    def rotateXY2(self):
        x0 = V[8][0]
        y0 = V[8][1]
        for i in range(len(V)):
            if (i == 8 or i == 7):
                continue
            vertex = V[i]
            x = vertex[0]
            y = vertex[1]
            R = numpy.sqrt(pow(x - x0, 2) + pow(y - y0, 2))
            angle = numpy.arccos((x - x0) / R)
            if i == 0 and angle <= 2 * numpy.pi / 3:
                self.t += 0.05
            new_angle = angle - self.t
            if new_angle <= 0:
                self.is_rotated = True
                break
            new_x = x0 + R * numpy.cos(new_angle)
            new_y = y0 + R * numpy.sin(new_angle)
            vertex[0] = new_x
            vertex[1] = new_y
        sleep(0.05)

    def update(self, unit):
        global V
        global T_PLANES
        V = [[-W, +W, +W],  # 0
             [-W, +W, -W],  # 1
             [+W, +W, -W],  # 2
             [+W, +W, +W],  # 3
             [0, 0, 0],  # 4
             [-W, -W, +W],  # 5
             [-W, -W, -W],  # 6
             [+W, -W, -W],  # 7
             [+W, -W, +W]]  # 8
        if self.unit == 2:
            global fall_direction
            dx, dz = fall_direction.xz(self.fall_t)
            dx /= 10000
            dz /= 10000
            self.x_shift = dx * 10
        for i in V:  # перемещение куба наверх
            # i[0] -= CUBE_WIDTH
            i[1] += 2 * CUBE_WIDTH
            i[2] += CUBE_WIDTH + CUBE_WIDTH + 0.5
            if unit == 1:
                i[0] += W * 2 * self.rotation_times
                # v[2] += W * 2 * (N - 1)
                # v[0] -= W * 2 * self.rotation_times
            if unit == 2:
                i[0] += dx * 10
                i[1] -= dz * 10
                pass
            if unit == 3:
                pass

        T_PLANES = [
            (V[0], V[1], V[4]),
            (V[1], V[6], V[4]),
            (V[6], V[5], V[4]),
            (V[5], V[0], V[4]),
            #
            (V[3], V[2], V[4]),
            (V[2], V[7], V[4]),
            (V[7], V[8], V[4]),
            (V[8], V[3], V[4]),
            #
            #
            (V[0], V[1], V[4]),
            (V[1], V[2], V[4]),
            (V[2], V[3], V[4]),
            (V[3], V[0], V[4]),
            #
            (V[7], V[8], V[4]),
            (V[6], V[7], V[4]),
            (V[5], V[6], V[4]),
            (V[8], V[5], V[4])
        ]
        self.is_rotated = False
        self.fall_t += 0.00001
        if self.unit == 1:
            self.rotation_times += 1
        # sleep(0.5)
