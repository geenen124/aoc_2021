import pathlib
import argparse

from day5.parse import parse_vents_input


def vent_overlaps(input_data: pathlib.Path) -> int:
    """
    Given an input data file, this finds the number of hydrothermal vent
    lines that overlap including diagonal lines!

    input_data: path to input data file

    returns the number of overlapping vents
    """
    vents = parse_vents_input(input_data)

    all_positions = set()
    overlapped_positions = set()
    for vent in vents:
        vent_positions_set = set(vent.get_whole_path(consider_diagonal=True))
        new_overlaps = vent_positions_set.intersection(all_positions)
        overlapped_positions.update(new_overlaps)
        all_positions.update(vent_positions_set)

    return len(overlapped_positions)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    num_overlaps = vent_overlaps(input_data_path)
    print(f"number of vent overlaps: {num_overlaps}")


if __name__ == "__main__":
    main()
