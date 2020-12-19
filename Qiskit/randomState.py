#your function is here
from math import cos, sin, pi
from random import randrange
def random_quantum_state():
    angle = randrange(360)
    angleRadian = 2 * pi * angle / 360
    return[cos(angleRadian), sin(angleRadian)]
