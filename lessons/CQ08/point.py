"""CQ08."""

from __future__ import annotations

__author__ = "730664337"


class Point:
    """Class for a point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        """Sets x and y when creating an instnace of the class."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales x and y by given factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scales x and y by given factor and creates a new point."""
        return_point: Point = Point(self.x, self.y)
        return_point.scale_by(factor)
        return return_point