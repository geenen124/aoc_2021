import pathlib
from typing import List


def parse_lanternfish_input(input_data: pathlib.Path) -> List[int]:
    buckets: List[int] = [0] * 9
    with input_data.open("r", encoding="utf-8") as input_lines:
        for i, line in enumerate(input_lines):
            fish = line.rstrip().split(",")
            for f in fish:
                buckets[int(f)] += 1

    return buckets
