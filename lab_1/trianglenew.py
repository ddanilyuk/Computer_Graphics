"""
*****************************
ONLY FOR TESTING NEW FEATURES
NOT USED
*****************************
"""
import math


class TriangleNew:
    """
    Default class for using in ornament
    """

    def __init__(self, width: int, height: int, startpoint: tuple):
        self.width = width
        self.height = height
        self.startpoint = startpoint

    def get_coords(self) -> tuple:
        a1 = self.startpoint[0] + (self.width / 2), self.startpoint[1]
        a2 = self.startpoint[0], self.startpoint[1] + self.height
        a3 = self.startpoint[0] + self.width, self.startpoint[1] + self.height
        return a1, a2, a3

    def get_diagonal_coord(self) -> tuple:
        aleft = self.a2[0], (self.a2[1] + self.a1[1]) / 2
        # aright = (self.a3[0], self.a3[1] - self.a1[1])

        return aleft[0], aleft[1], self.a3[0], self.a3[1]

    def get_center_coord(self) -> tuple:
        diag = self.get_diagonal_coord()
        return (diag[0] + diag[2]) / 2, (diag[1] + diag[3]) / 2

    def _get_corner_coords(self) -> tuple:
        diag = self.get_diagonal_coord()
        return diag[-2], diag[-1]

    def _transform(self, x: tuple, y: tuple, center: tuple, angle: float) -> tuple:
        x -= center[0]
        y -= center[1]

        temp_x = x * math.cos(angle) - y * math.sin(angle)
        temp_y = x * math.sin(angle) + y * math.cos(angle)

        return temp_x + center[0], temp_y + center[1]

    def rotate(self, angle: float, center=True) -> list:
        center = (self.a1, self.get_center_coord())[center]

        rotated_coords = [
            self._transform(x, y, center, angle) for x, y in self.get_coords()
        ]

        return rotated_coords

    def creatr_figure(
            self, canv, angle: float, color: str,
            center: bool = True, k: int = 0
    ):
        m = self.rotate(angle, center=center)

        canv.create_line(
            m[0][0] - k, m[0][1] - k, m[1][0] - k, m[1][1] - k, fill=color)
        canv.create_line(
            m[0][0] - k, m[0][1] - k, m[2][0] - k, m[2][1] - k, fill=color)
        # canv.create_line( m[2][0] - k, m[2][1] - k, m[-1][0] - k, m[-1][1] - k, fill="Yellow")
        canv.create_line(
            m[1][0] - k, m[1][1] - k, m[-1][0] - k, m[-1][1] - k, fill=color)

        canv.pack()
