from dataclasses import dataclass
from typing import List


@dataclass
class Position:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Vent:
    start: Position
    end: Position

    def get_whole_path(self, consider_diagonal=False) -> List[Position]:
        if self.start.x == self.end.x:
            # horizontal
            s_y, e_y = min(self.start.y, self.end.y), max(self.start.y, self.end.y)
            return [Position(self.start.x, y) for y in range(s_y, e_y + 1)]
        elif self.start.y == self.end.y:
            # vertical
            s_x, e_x = min(self.start.x, self.end.x), max(self.start.x, self.end.x)
            return [Position(x, self.start.y) for x in range(s_x, e_x + 1)]
        else:
            # diagonal
            if consider_diagonal:
                return self.__get_diagonal_positions()
            else:
                return []

    def __get_diagonal_positions(self) -> List[Position]:
        x_increasing = self.start.x < self.end.x
        y_increasing = self.start.y < self.end.y

        cur_x = self.start.x
        cur_y = self.start.y
        distance = abs(self.start.x - self.end.x) + 1
        return [
            Position(
                cur_x + i if x_increasing else cur_x - i,
                cur_y + i if y_increasing else cur_y - i
            )
            for i in range(distance)
        ]
