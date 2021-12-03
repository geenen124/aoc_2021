import pathlib
import argparse
from collections import defaultdict


def power_consumption(input_data: pathlib.Path) -> (int, int):
    """
    Given an input data file, this parses a binary diagnostic report
    to calculate the gamma and epsilon rates for power consumption

    input_data: path to input data file

    returns a tuple of the power consumption as (gamma, epsilon)
    """
    position_freqs = defaultdict(lambda: [0, 0])
    max_len = 0

    with input_data.open("r", encoding="utf-8") as input_lines:
        for line in input_lines:
            binary = line.rstrip()
            max_len = max(max_len, len(binary))
            for i in range(1, len(binary) + 1):
                position_freqs[i][int(binary[-i])] += 1

    gamma_bin = "".join([str(max(range(2), key=position_freqs[bin_ind].__getitem__)) for bin_ind in range(max_len, 0, -1)])
    epsilon_bin = "".join([str(min(range(2), key=position_freqs[bin_ind].__getitem__)) for bin_ind in range(max_len, 0, -1)])

    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)

    return gamma, epsilon


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    gamma, epsilon = power_consumption(input_data_path)
    print(f"power consumption values: {gamma}, {epsilon}")
    print(f"power consumption: {gamma*epsilon}")


if __name__ == "__main__":
    main()
