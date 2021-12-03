import pathlib
import argparse
from collections import defaultdict
from typing import List


def life_support(input_data: pathlib.Path) -> (int, int):
    """
    Given an input data file, this parses a binary diagnostic report
    to calculate the oxygen generator and CO2 scrubber rates for life support

    input_data: path to input data file

    returns a tuple of the life sypport numbers as (oxygen_generator, co2_scrubber)
    """

    def split_by_freqs_at_pos(to_split: List[str], position: int):
        position_freqs = [0, 0]
        bit_in_position = [list(), list()]
        for s in to_split:
            s_bit = int(s[-position])
            position_freqs[s_bit] += 1
            bit_in_position[s_bit].append(s)

        return position_freqs, bit_in_position

    max_len = 0
    all_readings = []
    with input_data.open("r", encoding="utf-8") as input_lines:
        for line in input_lines:
            binary = line.rstrip()
            max_len = max(max_len, len(binary))
            all_readings.append(binary)

    oxygen_readings = all_readings
    for bin_ind in range(max_len, 0, -1):
        if len(oxygen_readings) == 1:
            break

        cur_pos_freqs, bit_in_position = split_by_freqs_at_pos(oxygen_readings, bin_ind)
        max_ind = cur_pos_freqs.index(max(cur_pos_freqs))
        if max(cur_pos_freqs) == min(cur_pos_freqs):
            max_ind = 1

        oxygen_readings = bit_in_position[max_ind]

    oxygen_bin = oxygen_readings[0]

    co2_scrubber_readings = all_readings
    for bin_ind in range(max_len, 0, -1):
        if len(co2_scrubber_readings) == 1:
            break

        cur_pos_freqs, bit_in_position = split_by_freqs_at_pos(co2_scrubber_readings, bin_ind)
        min_ind = cur_pos_freqs.index(min(cur_pos_freqs))
        if max(cur_pos_freqs) == min(cur_pos_freqs):
            min_ind = 0
        co2_scrubber_readings = bit_in_position[min_ind]

    co2_scrubber_bin = co2_scrubber_readings[0]

    oxygen = int(oxygen_bin, 2)
    co2 = int(co2_scrubber_bin, 2)

    return oxygen, co2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_file")

    args = parser.parse_args()

    input_data_path = pathlib.Path(args.input_data_file)

    if not input_data_path.is_file():
        raise ValueError("input_data_file must be a valid file!")

    oxygen, co2 = life_support(input_data_path)
    print(f"life support values: {oxygen}, {co2}")
    print(f"life support rating: {oxygen*co2}")


if __name__ == "__main__":
    main()
