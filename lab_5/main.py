import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import fabs
import random


plt.style.use('dark_background')

# fig = plt.figure
fig, ax = plt.subplots()
ax = plt.axes(xlim=(-60, 60), ylim=(-60, 60))
line1, = ax.plot([], [], lw=2, color='blue')
line2, = ax.plot([], [], lw=2, color='violet')
ball1, = ax.plot([], [], color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=33)
ball2, = ax.plot([], [], color='violet', marker='o', linestyle='dashed', linewidth=2, markersize=33)


# Функция инициализации.
def init():
    # создение пустого графа.
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2,


xdata, ydata = [], []
xdata2, ydata2 = [], []

# Color for random choosing
colors = ['white', 'yellow', 'red', 'brown', 'blue', 'violet', 'orange']


# функция анимации
def animate(i):
    tt = 0.1 * i
    tt2 = 0.05 * i

    print(i)

    # x, y данные на графике

    # First trajectory
    x1 = 40 * np.sin(tt) ** 3
    y1 = 40 * np.cos(tt) ** 3

    bx1 = 40 * np.sin(tt) ** 3
    by1 = 40 * np.cos(tt) ** 3

    # Second trajectory
    x2 = 40 * np.sin(tt2) ** 3 + 10
    y2 = 40 * np.cos(tt2) ** 3 + 6

    bx2 = 40 * np.sin(tt2) ** 3 + 10
    by2 = 40 * np.cos(tt2) ** 3 + 6

    # добавление новых точек в список точек осей x, y
    xdata.append(x1)
    ydata.append(y1)
    line1.set_data(xdata, ydata)

    ball1.set_data(bx1, by1)

    xdata2.append(x2)
    ydata2.append(y2)
    line2.set_data(xdata2, ydata2)
    ball2.set_data(bx2, by2)

    difference_x = fabs(x1 - x2) * 10
    difference_y = fabs(y1 - y2) * 10

    # print(difference_x, "\n", difference_y)

    if (difference_x < 120 and difference_y < 120):
        new_color1 = colors[random.randint(0, len(colors)-1)]
        new_color2 = colors[random.randint(0, len(colors)-1)]
        ball1.set(color=new_color1)
        ball2.set(color=new_color2)


        print("YES")

    return line1, line2, ball1, ball2


# Заголовок анимации
plt.title('Lab_5')
# Скрываем лишние данные
plt.axis('off')


# Вызов анимации.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=70, blit=True)

plt.show()
