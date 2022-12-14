import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import random

plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True

width = 0.8  # size of edge, between 0 and 1
height = math.sqrt(width ** 2 - (width / 2) ** 2)  # height of the equilateral triangle

xpad = (1 -  width) / 2
ypad = (1 - height) / 2

# the outlining triangle
triangle = [(xpad, ypad), (1 - xpad, ypad), (0.5, 1 - ypad)]

xdots = [x for x, _ in triangle]
ydots = [y for _, y in triangle]

fig, ax = plt.subplots()

def point_on_triangle(pt1, pt2, pt3):
    """Random point on the triangle with vertices pt1, pt2 and pt3."""
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (
        s * pt1[0] + t * pt2[0] + u * pt3[0],
        s * pt1[1] + t * pt2[1] + u * pt3[1],
    )

last = point_on_triangle(*triangle)
xdots.append(last[0])
ydots.append(last[1])

ax = fig.add_subplot(111, aspect = 'equal', autoscale_on = False, xlim = (0, 1), ylim = (0, 1))
colors = [0.9] * len(xdots)

def animate(i):
    global last, colors, ax

    orig_index = random.randrange(len(triangle))
    orig = triangle[orig_index]
    half = ((orig[0] + last[0]) / 2, (orig[1] + last[1]) / 2)
    xdots.append(half[0])
    ydots.append(half[1])

    colors.append(0.1)  # new dot
    colors[-2] = 0.2
    colors[orig_index] = 0.2

    last = half

    ax.scatter(xdots, ydots, s = 5, c = colors, cmap = "Set1")

    colors[-1] = 0.9
    colors[-2] = 0.9
    colors[orig_index] = 0.9

anim = animation.FuncAnimation(fig, animate, interval = 0, frames = range(1000))

def onpress(event):
    global pause
    if pause: anim.event_source.start() # resume
    else:     anim.event_source.stop()  # pause
    pause = not pause

fig.canvas.mpl_connect('key_press_event', onpress)
pause = False

plt.show()
# anim.save('animation.gif', writer='pillow')
