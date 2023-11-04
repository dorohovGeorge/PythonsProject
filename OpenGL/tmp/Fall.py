import numpy as np


class Fall(object):

    def __init__(self, x=0, z=0, v0=0):
        self.__z = z
        self.__x = x
        self.__v0 = v0
        self.g = 9.8066 # 9.8066

    def xz(self, t):
        if self.__v0 > 0:
            self.__v0 -= self.g * t
        else:
            self.__v0 = 0.001
        t *= 10000
        return self.__v0 * t, self.__v0 * t + (self.g * (t ** 2)) / 2

    def max_time(self):
        return np.sqrt(2 * self.__z / self.g)
