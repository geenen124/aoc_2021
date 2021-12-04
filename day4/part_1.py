import pathlib
import argparse

from day4.bingo_board import BingoBoard
from day4.parse import parse_bingo_input


def fastest_bingo(input_data: pathlib.Path) -> (BingoBoard, int):
    """
    Given an input data file, this finds the bingo board that
    will win first for the provided number draws, along with the winning draw

    input_data: path to input data file

    returns a tuple of (the fastest winning bingo board, winning draw)
    """
    draws, bingo_boards = parse_bingo_input(input_data)
    for draw in draws:
        for bingo_board in bingo_boards:
            bingo_board.mark(draw)
            if bingo_board.check_win():
                return bingo_board, draw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    fastest_board, winning_draw = fastest_bingo(input_data_path)
    print(f"winning draw: {winning_draw}")
    print(f"final score: {sum(fastest_board.get_unmarked())*winning_draw}")


if __name__ == "__main__":
    main()
