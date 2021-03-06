import pathlib
import argparse
from collections import deque


def run_sweep(input_data: pathlib.Path, window_size: int) -> int:
    """
    Given an input data file, this checks the number of sliding windows of
    depth measurements that are larger than the previous sliding window

    input_data: path to input data file
    window_size: size of the sliding window to check

    return total number of increases
    """
    total_increases = 0
    window = deque()

    with input_data.open("r", encoding="utf-8") as input_lines:
        for line in input_lines:
            depth = int(line.rstrip())
            if len(window) == window_size:
                prev = window.popleft()
                if depth > prev:
                    total_increases += 1
            window.append(depth)

    return total_increases



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    total_increases = run_sweep(input_data_path, 3)
    print(f"Total larger sliding windows: {total_increases}")


if __name__ == "__main__":
    main()
