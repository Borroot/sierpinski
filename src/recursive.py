import pyglet
import math
import time

size = 1500
window = pyglet.window.Window(size, size)

width = 0.8  # size of edge, between 0 and 1
height = math.sqrt(width ** 2 - (width / 2) ** 2)  # height of the equilateral triangle

xpad = size * ((1 -  width) / 2)
ypad = size * ((1 - height) / 2)

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


    def draw_void(self):
        """Draw the void sub triangle."""
        x1 = (self.x1 + self.x2) / 2
        x2 = (self.x2 + self.x3) / 2
        x3 = (self.x3 + self.x1) / 2
        y1 = (self.y1 + self.y2) / 2
        y2 = (self.y2 + self.y3) / 2
        y3 = (self.y3 + self.y1) / 2
        pyglet.shapes.Triangle(x1, y1, x2, y2, x3, y3, color = (0, 0, 0)).draw()

        """Return the other three sub triangles."""
        return [
            Triangle(self.x1, self.y1, x1, y1, x3, y3),
            Triangle(x1, y1, self.x2, self.y2, x2, y2),
            Triangle(x3, y3, x2, y2, self.x3, self.y3),
        ]


    def draw(self):
        """Draw the triangle itself."""
        pyglet.shapes.Triangle(
            self.x1, self.y1, self.x2, self.y2, self.x3, self.y3,
            color = (50, 250, 50)
        ).draw()


# the outlining triangle
triangle = Triangle(xpad, ypad, size - xpad, ypad, size // 2, size - ypad)
triangle.draw()

triangles = triangle.draw_void()
pause = False

@window.event
def on_draw():
    global triangles
    if pause: return

    for _ in range(2):  # adjust to change speed
        triangle = triangles.pop(0)
        triangles.extend(triangle.draw_void())

@window.event
def on_key_press(symbol, modifiers):
    global pause
    pause = not pause


pyglet.app.run()
