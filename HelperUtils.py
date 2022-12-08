import json


def open_file(file: str):
    with open(file, "r") as f:
        lines = f.readlines()

    return lines


def write_answers(day: int, part_one_ans=None, part_two_ans=None, file_path=None):
    answers = {f"Day {day}": {"Part 1": part_one_ans, "Part 2": part_two_ans}}

    with open(file_path, "w") as outfile:
        json.dump(answers, outfile, indent=4)
