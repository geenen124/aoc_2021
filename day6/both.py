import pathlib
import argparse

from day6.parse import parse_lanternfish_input


def simulate_lanternfish(input_data: pathlib.Path, num_days: int) -> int:
    """
    Given an input data file, this finds the number of lanternfish that exist after :num_days!

    input_data: path to input data file
    num_days: number of days that will pass

    returns the number of lanternfish at the end of the time period
    """
    lantern_fish_buckets = parse_lanternfish_input(input_data)

    current_0 = 0

    for day in range(num_days):
        next_6 = (current_0 - 2) % len(lantern_fish_buckets)
        lantern_fish_buckets[next_6] += lantern_fish_buckets[current_0]
        current_0 = (current_0 + 1) % len(lantern_fish_buckets)

    return sum(lantern_fish_buckets)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")
    parser.add_argument("num_days", type=int)

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)
    num_days = args.num_days

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    num_lanternfish = simulate_lanternfish(input_data_path, num_days)
    print(f"number of lanternfish after {num_days} days: {num_lanternfish}")


if __name__ == "__main__":
    main()
