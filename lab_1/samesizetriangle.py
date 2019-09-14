import math


class SameSizeTriangle:
    """
    Default class for using in ornament
    """

    def __init__(self, size: int, startpoint: tuple):
        self.size = size
        self.startpoint = startpoint

    def get_coords(self) -> tuple:
        a1 = self.startpoint[0] + (self.size / 2), self.startpoint[1]
        a2 = self.startpoint[0] + self.size, \
             self.startpoint[1] + ((self.size * math.sqrt(3)) / 2)
        a3 = self.startpoint[0], self.startpoint[1] + ((self.size * math.sqrt(3)) / 2)
        return a1, a2, a3

    def get_center_coord(self) -> tuple:
        x = self.get_coords()[0][0]
        y = self.get_coords()[0][1] + (self.size / math.sqrt(3))
        return x, y

    def _transform(self, x: tuple, y: tuple, center: tuple, angle: float) -> tuple:
        x -= center[0]
        y -= center[1]

        temp_x = x * math.cos(angle) - y * math.sin(angle)
        temp_y = x * math.sin(angle) + y * math.cos(angle)

        return temp_x + center[0], temp_y + center[1]

    def rotate(self, angle: float, center=True) -> list:
        center = (self.get_coords()[0], self.get_center_coord())[center]

        rotated_coords = [
            self._transform(x, y, center, angle) for x, y in self.get_coords()
        ]

        return rotated_coords

    def create_square(
            self, canv, angle: float, color: str,
            center: bool = True, k: int = 0
    ):
        m = self.rotate(angle, center=center)

        canv.create_line(
            m[0][0] - k, m[0][1] - k, m[1][0] - k, m[1][1] - k, fill=color)
        canv.create_line(
            m[0][0] - k, m[0][1] - k, m[2][0] - k, m[2][1] - k, fill=color)
        canv.create_line(
            m[1][0] - k, m[1][1] - k, m[-1][0] - k, m[-1][1] - k, fill=color)

        canv.pack()
