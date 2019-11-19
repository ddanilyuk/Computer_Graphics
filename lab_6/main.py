import tkinter as tk
import math
import time


def s(x, y, z, dist):
    return 1 / 2 + x * dist / (z + dist) + 500, 1 / 2 - y * dist / (z + dist) + 500


def matrfor_x(x, y, z, fi):
    return x, y * math.cos(fi) - z * math.sin(fi), y * math.sin(fi) + z * math.cos(fi)


def matrfor_y(x, y, z, fi):
    return x * math.cos(fi) + z * math.sin(fi), y, -x * math.sin(fi) + z * math.cos(fi)


def matrfor_z(x, y, z, fi):
    return x * math.cos(fi) - y * math.sin(fi), x * math.sin(fi) + y * math.cos(fi), z


def drawFigure(w, h):
    th = (w * math.sqrt(3)) / 2
    A = (0, th * (2/3), -h)
    B = (-w / 2, - th * (1/3), -h)
    C = (w / 2, - th * (1/3), -h)

    SA = (0, (th * (2/3)) / 3, 0)
    SB = (-w / 6, (- th * (1/3)) /3, 0)
    SC = (w / 6, (- th * (1/3))/3, 0)

    a = [A, B, C, SC, SB, B, SB, SA, A,  SA, SC, SA, A, C]
    return a


root = tk.Tk()
root.geometry("1000x1000")
canv = tk.Canvas(root, bg='white', width=1000, height=1000)
dist = 1000
canv.place(x=0, y=0)
j = 0

while True:
    j += 1
    canv.delete(j - 1)
    a = drawFigure(250, 250)
    for i in range(len(a)):
        a[i] = matrfor_x(a[i][0], a[i][1], a[i][2], j / 100)  # вращаем относительно оси икс
        a[i] = matrfor_y(a[i][0], a[i][1], a[i][2], j / 100)  # игрек
        # a[i] = matrfor_z(a[i][0], a[i][1], a[i][2], j / 100)  # зет
        a[i] = s(a[i][0], a[i][1], a[i][2], dist)
    canv.create_line(a)
    canv.update()
    time.sleep(0.01)

root.mainloop()
