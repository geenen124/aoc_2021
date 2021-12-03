import pathlib
import argparse

from day2.command import parse_command_from_navigation_line


def navigate(input_data: pathlib.Path) -> (int, int):
    """
    Given an input data file, this follows the course of the submarine
    and returns its final position

    input_data: path to input data file

    returns a tuple of the final position as (horizontal position, depth)
    """
    horizontal, depth, aim = 0, 0, 0

    with input_data.open("r", encoding="utf-8") as input_lines:
        for line in input_lines:
            command = parse_command_from_navigation_line(line.rstrip())
            match command.direction:
                case "forward":
                    horizontal += command.increment
                    depth += (aim * command.increment)
                case "down":
                    aim += command.increment
                case "up":
                    aim -= command.increment

    return horizontal, depth


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    horizontal, depth = navigate(input_data_path)
    print(f"Final position: {horizontal}, {depth}")
    print(f"Final position multiplied: {horizontal*depth}")


if __name__ == "__main__":
    main()
