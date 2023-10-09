import os, time
from math_lib import *

width, height = os.get_terminal_size()
height -= 2
pixelBuffer = ['*']*(width*height)

def draw():
    print(''.join(pixelBuffer), end='')

def clear(char):
    for i in range (width*height):
        pixelBuffer[i] = char

def putPixel(v, pixel):
    x1, y1 = round(v.x), round(v.y)

    if 0 <= x1 < width and 0 <= y1 < height:
        pixelBuffer[y1 * width + x1] = pixel

def eq(p, a, b):
    return (a.x - p.x) * (b.y - p.y) - (a.y - p.y) * (b.x - p.x)

def createTriangle(tri, pixel):
    xmin = round(min(tri.p1.x, tri.p2.x, tri.p3.x))
    xmax = round(max(tri.p1.x, tri.p2.x, tri.p3.x)) + 1
    ymin = round(min(tri.p1.y, tri.p2.y, tri.p3.y))
    ymax = round(max(tri.p1.y, tri.p2.y, tri.p3.y)) + 1

    for y in range (ymin, ymax):
        if 0 <= y < height:
            for x in range (xmin, xmax):
                if 0 <= x < width:
                    pos = vec2(x, y)
                    w1 = eq(pos, tri.p3, tri.p1)
                    w2 = eq(pos, tri.p1, tri.p2)
                    w3 = eq(pos, tri.p2, tri.p3)
                    if  (w1 >= 0 and w2 >= 0 and w3 >= 0) or (-w1 >= 0 and -w2 >= 0 and -w3 >= 0):
                        putPixel(pos, pixel)
