import tkinter as tk
import numpy as np
import argparse
import random

from lab_5.movingModel import MovingModel as MV_model


def main(A, B, R, size) -> None:
    """
    Load window with 2 moving figures

    :param A: size of A
    :param B: size of B
    :param R: size of R
    :param size: scale size
    """

    # Creating root and canvas
    window = tk.Tk()
    canvas = tk.Canvas(window, width=1200, height=900, bg='lightgrey')
    canvas.pack()

    # Formula for figure coords
    formula_for_coords = {
        'x': lambda t: (A * R * (np.sin(t)) ** 3) * size,
        'y': lambda t: (B * R * (np.cos(t)) ** 3) * size,
    }

    # Some figures's params
    speed_1 = {'x': 10, 'y': 5}
    speed_2 = {'x': 5, 'y': 10}

    # Color for random choosing
    colors = ['black', 'yellow', 'red', 'brown', 'Navy Blue', 'violet', 'orange']

    # Create 2 models with different start points
    model1 = MV_model(
        canvas, formula_for_coords, speed_1,
        center=(random.randint(100, 400), random.randint(100, 300)),
        timeon=25)
    model2 = MV_model(
        canvas, formula_for_coords, speed_2,
        center=(random.randint(600, 1000), random.randint(500, 800)),
        timeon=25)

    def check_distance():
        """
        Check if figures are close enough
        and change their speed to opposite by direction
        """
        center1 = model1.get_center()
        center2 = model2.get_center()

        if (
                abs(center1[0] - center2[0]) <= 180 and
                abs(center1[1] - center2[1]) <= 180
        ):
            model1.change_direction(x=True, y=True)
            model1.change_color(
                colors[random.randint(0, len(colors)) - 1])

            model2.change_direction(x=True, y=True)
            model2.change_color(
                colors[random.randint(0, len(colors) - 1)])

        canvas.after(50, check_distance)

    # Set timer for checking
    canvas.after(50, check_distance)

    # Start program
    window.mainloop()


# Some cli params handles
if __name__ == '__main__':
    parser = argparse.ArgumentParser('Built 2 moving figures')

    parser.add_argument(
        '--A', type=float, default=10)
    parser.add_argument(
        '--B', type=float, default=20)
    parser.add_argument(
        '--R', type=float, default=5)
    parser.add_argument(
        '--size', help="Scale your chart", type=float, default=1)

    args = parser.parse_args()

    # Starting point of main script with given params
    main(args.A, args.B, args.R, args.size)
