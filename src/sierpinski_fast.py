import pyglet
import math
import random

size = 1500
window = pyglet.window.Window(size, size)

width = 0.8  # size of edge, between 0 and 1
height = math.sqrt(width ** 2 - (width / 2) ** 2)  # height of the equilateral triangle

xpad = size * ((1 -  width) / 2)
ypad = size * ((1 - height) / 2)

# the outlining triangle
triangle = [(xpad, ypad), (size - xpad, ypad), (size // 2, size - ypad)]
dots = [p for p in triangle]

def point_on_triangle(pt1, pt2, pt3):
    """Random point on the triangle with vertices pt1, pt2 and pt3."""
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (
        s * pt1[0] + t * pt2[0] + u * pt3[0],
        s * pt1[1] + t * pt2[1] + u * pt3[1],
    )

def init_draw():
    # draw the outlining triangle
    for corner in triangle:
        pyglet.shapes.Circle(*corner, radius = 3, color = (30, 225, 200)).draw()

    # create a random last point and draw it
    pyglet.shapes.Circle(*last, radius=3, color=(50, 225, 30)).draw()

last = point_on_triangle(*triangle)
init_draw()

pause = True

@window.event
def on_key_press(symbol, modifiers):
    global pause, last

    if symbol == pyglet.window.key.C:
        window.clear()
        last = point_on_triangle(*triangle)
        init_draw()
    else:
        pause = not pause

@window.event
def on_draw():
    global last
    if pause: return

    orig_index = random.randrange(len(triangle))
    orig = triangle[orig_index]
    half = ((orig[0] + last[0]) / 2, (orig[1] + last[1]) / 2)
    last = half
    pyglet.shapes.Circle(*half, radius = 2, color = (50, 225, 30)).draw()

pyglet.app.run()
