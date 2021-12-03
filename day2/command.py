from dataclasses import dataclass


@dataclass
class Command:
    direction: str
    increment: int


def parse_command_from_navigation_line(line: str) -> Command:
    line_parts = line.split(" ")
    if len(line_parts) != 2:
        raise ValueError("Invalid Navigation Line")

    return Command(line_parts[0], int(line_parts[1]))
