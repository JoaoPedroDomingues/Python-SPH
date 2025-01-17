import random

import physics
import setting
from const import *


'''
SETUPS n BY n GRID OF PARTICLES 
'''
def setup_grid(num) -> None:
    x_init = X_MID - num * SPC / 2
    y_init = Y_MID - num * SPC / 2

    y = y_init
    id = 0

    for i in range(num):
        x = x_init
        for j in range(num):
            physics.particles.append(
                physics.Particle(
                    id,
                    x,
                    y
                )
            )
            id += 1
            x += SPC
        y += SPC

'''
SPAWNS n^2 PARTICLES RANDOMLY
'''
def setup_random(num) -> None: 
    num = num ** 2

    for i in range(num):
        x = random.randrange(0, X_RES, 1)
        y = random.randrange(0, Y_RES, 1)

        physics.particles.append(
            physics.Particle(
                i,
                x,
                y
            )
        )

if setting.SETUP_SETTING == 0:
    setup_grid(setting.NUM)
elif setting.SETUP_SETTING == 1:
    setup_random(setting.NUM)

