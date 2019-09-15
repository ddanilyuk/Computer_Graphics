import tkinter as tk
import math
import argparse
from lab_1 import SameSizeTriangle as model


def main(n, m):
    window = tk.Tk()

    # VARIABLES
    screenSize = (700, 700)  # (width, height)

    size1 = 400  # Mark: - Size of larger figure
    startPoint1 = (140, 120)  # (x, y)  Start point of larger figure
    color1 = "Orange"

    size2 = 110  # Mark: - Size of smaller figure
    color2 = "Navy Blue"

    '''
        Mark: - the start point coordinates of the smaller figure
        are calculated automatically (should be in the center) 
        depending on the coordinates larger figure
    '''
    canvas = tk.Canvas(window, width=screenSize[0], height=screenSize[1])

    coordinates1 = [
        size1, (startPoint1[0], startPoint1[1])
    ]
    mdl1 = model(*coordinates1)

    coordinates2 = [
        size2, (mdl1.get_center_coord()[0] - (size2 / 2), mdl1.get_center_coord()[1])
    ]
    mdl2 = model(*coordinates2)

    for angle in [math.pi / n * i for i in range(-n, n)]:
        mdl1.create_figure(canvas, angle, color1, center=True)

    for angle in [math.pi / m * i for i in range(-m, m)]:
        mdl2.create_figure(canvas, angle, color2, center=False)

    window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Built different charts with sqaures acording to params')
    parser.add_argument(
        '--n', help='Initialize num for center rotation', type=int, default=5)
    parser.add_argument(
        '--m', help='Initialize num for corner rotation', type=int, default=12)

    args = parser.parse_args()
    main(args.n, args.m)
