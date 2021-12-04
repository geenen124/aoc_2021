import pathlib
from typing import List

from day4.bingo_board import BingoBoard


def parse_bingo_input(input_data: pathlib.Path) -> (List[int], List[BingoBoard]):
    inputs: List[int] = []
    boards: List[BingoBoard] = []
    with input_data.open("r", encoding="utf-8") as input_lines:
        current_board = []
        for i, line in enumerate(input_lines):
            current_line = line.rstrip()
            if len(current_line) > 0:
                if i == 0:
                    inputs = [int(x) for x in current_line.split(",")]
                else:
                    current_board.append([int(x) for x in current_line.split()])
                    if len(current_board) == 5:
                        boards.append(BingoBoard(current_board.copy()))
                        current_board.clear()

    return inputs, boards
