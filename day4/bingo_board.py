from typing import List, Set


class BingoBoard:
    BOARD_SIZE = 5
    board: List[List[int]]
    board_contents: Set[int]
    marked: Set[int]

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.board_contents = set().union(*[set(x) for x in board])
        self.marked = set()

    def mark(self, to_mark: int) -> None:
        if to_mark in self.board_contents:
            self.marked.add(to_mark)

    def check_win(self) -> bool:
        if len(self.marked) < self.BOARD_SIZE:
            return False

        for row in range(self.BOARD_SIZE):
            if all([(self.board[row][col] in self.marked) for col in range(self.BOARD_SIZE)]):
                return True

        for col in range(self.BOARD_SIZE):
            if all([(self.board[row][col] in self.marked) for row in range(self.BOARD_SIZE)]):
                return True

        return False

    def get_unmarked(self) -> List[int]:
        return list(self.board_contents - self.marked)
