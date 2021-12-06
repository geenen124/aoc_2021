import pathlib
from typing import List

from day5.vent import Vent, Position


def parse_vents_input(input_data: pathlib.Path):
    vents: List[Vent] = []
    with input_data.open("r", encoding="utf-8") as input_lines:
        for i, line in enumerate(input_lines):
            current_line_arr = line.rstrip().split(" -> ")
            start_str, end_str = current_line_arr[0], current_line_arr[1]
            start_arr = [int(n) for n in start_str.split(",")]
            end_arr = [int(n) for n in end_str.split(",")]
            vents.append(
                Vent(
                    Position(start_arr[0], start_arr[1]),
                    Position(end_arr[0], end_arr[1])
                )
            )
    return vents