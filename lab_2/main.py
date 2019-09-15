import argparse
import math
import tkinter as tk
from lab_2.figure import Figure as figure


def main(n, m):
    window = tk.Tk()
    window.title("lab #2")

    # VARIABLES
    screenSize = (700, 700)  # (width, height)
    canvas = tk.Canvas(window, width=screenSize[0], height=screenSize[1])

    # Here is 4 pre-sets (choose from 1 to 5) or do your own figure
    preSetNumber = 5

    if preSetNumber == 1:
        mdl = figure(20, 10, 15, 5, (350, 350))
        mdl.createFigure(canvas, 0, "Red")

    elif preSetNumber == 2:
        n = 5
        m = 5

        mdl1 = figure(20, 20, 6, 5, (350, 350))
        mdl2 = figure(20, 20, 12, 5, (350, 350))

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl1.createFigure(canvas, angle, "Blue", turnPoint=0)

        for angle in [math.pi / n * i for i in range(-m, m)]:
            mdl2.createFigure(canvas, angle, "Orange", turnPoint=0)

    elif preSetNumber == 3:
        n = 4

        mdl = figure(20, 20, 6, 5, (230, 230))

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl.createFigure(canvas, angle, "Navy Blue", turnPoint=1)

    elif preSetNumber == 4:
        n = 3

        mdl = figure(20, 20, 6, 5, (250, 250))

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl.createFigure(canvas, angle, "Blue", turnPoint=2)

    elif preSetNumber == 5:
        n = 60

        mdl = figure(20, 20, 9, 5, (250, 250))

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl.createFigure(canvas, angle, "magenta", turnPoint=2)

    window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Built different charts with figures according to params')
    parser.add_argument(
        '--n', help='Initialize num for first figure rotation', type=int, default=4)
    parser.add_argument(
        '--m', help='Initialize num for second figure rotation', type=int, default=5)

    args = parser.parse_args()
    main(args.n, args.m)
