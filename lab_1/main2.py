"""
*****************************
ONLY FOR TESTING NEW FEATURES
NOT USED
*****************************
"""

import tkinter as tk
import math
import argparse
from lab_1 import Triangle as model
from lab_1 import SameSizeTriangle as model2


def getheight(size: int) -> float:
    return (size * math.sqrt(3)) / 2


def main(n, m, colors_n, colors_m):
    window = tk.Tk()

    SCALE = 1.2
    coords = [  # (x1, y1), (x2, y2), (x3, y3), (x4, y4)
        (150 * SCALE, 200 * SCALE), (100 * SCALE, 300 * SCALE),
        (200 * SCALE, 300 * SCALE)
    ]

    coords2 = [
        (150 * SCALE, 275 * SCALE), (90 * SCALE, 395 * SCALE),
        (210 * SCALE, 395 * SCALE)
    ]

    mdl = model(*coords)
    mdl2 = model(*coords2)

    coords3 = [
        400, (200, 200)
    ]
    mdl3 = model2(*coords3)

    size4 = 100
    coords4 = [
        size4, (mdl3.get_center_coord()[0] - (size4 / 2), mdl3.get_center_coord()[1])
    ]

    mdl4 = model2(*coords4)

    canv = tk.Canvas(window, width=700, height=700)
    switch = True

    colors_n = ["Blue", "Green"]

    # mdl.create_square(canv, 0, color="Blue", center=True)
    # mdl.create_square(canv, 0.5, colors_m[0], center=True)
    # mdl.create_square(canv, 1, colors_m[0], center=True)
    # mdl.create_square(canv, 1.5, colors_m[0], center=True)
    # mdl.create_square(canv, 2, colors_m[0], center=True)

    for angle in [math.pi / n * i for i in range(-n, n)]:
        mdl3.create_square(
            canv, angle, colors_n[0], center=True)
        # switch = not switch

    for angle in [math.pi / m * i for i in range(-m, m)]:
        mdl4.create_square(
            canv, angle, colors_n[1], center=False)
        # switch = not switch

    window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Built different charts with sqaures acording to params')
    parser.add_argument(
        '--n', help='Initialize num for center rotation', type=int, default=5)
    parser.add_argument(
        '--m', help='Initialize num for corner rotation', type=int, default=16)
    parser.add_argument(
        '--colors_inner', help='Initialize colors for center rotation',
        type=str, default=['black', 'black'], nargs=2)
    parser.add_argument(
        '--colors_outer', help='Initialize colors for corner rotation',
        type=str, default=['black', 'black'], nargs=2)

    args = parser.parse_args()
    main(args.n, args.m, args.colors_inner, args.colors_outer)
