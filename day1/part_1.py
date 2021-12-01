import pathlib
import argparse


def run_sweep(input_data: pathlib.Path) -> int:
    """
    Given an input data file, this checks the number of 
    depth measurements that are larger than the previous measurement.

    input_data: path to input data file

    returns total number of increases
    """
    total_increases = 0
    previous_depth = None

    with input_data.open("r", encoding="utf-8") as input_lines:
        for line in input_lines:
            depth = int(line.rstrip())
            if previous_depth and (depth - previous_depth) > 0:
                total_increases += 1
            previous_depth = depth

    return total_increases



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    total_increases = run_sweep(input_data_path)
    print(f"Total larger measurements: {total_increases}")


if __name__ == "__main__":
    main()
