from math import hypot

from const import *

'''
MATH FUCNTION FOR CALCULATION OF INFLUENCE IN DENSITY WITH DISTANCE
'''
def smothing_kernel(dst) -> float:
    if dst >= S_RAD:
        return 0
    
    return (S_RAD - dst) ** 2 / VOLUME

'''
DERIVATIVE OF THE PREVIOUS FUNCTION
'''
def smothing_kernel_gradient(dst) -> float:
    if dst >= S_RAD:
        return 0
    
    return (dst - S_RAD) * SCALE

'''
MATH FUNCTION TO CALCULATE DISTANCE BETWEEN TWO POINTS
'''
def distance(p1x, p2x, p1y, p2y) -> float:
    return hypot(p2x - p1x, p2y - p1y)
