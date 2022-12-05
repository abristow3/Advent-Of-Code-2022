from enum import Enum
from HelperUtils import open_file, write_answers

points_dict = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}


class StaticRules(Enum):
    LOST = 0
    DRAW = 3
    WIN = 6
    # Shape : Shape loses to
    ROCK = "PAPER"
    PAPER = "SCISSORS"
    SCISSORS = "ROCK"
    A = "ROCK"
    B = "PAPER"
    C = "SCISSORS"


class PartOneRules(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"
    A = "X"
    B = "Y"
    C = "Z"


class PartTwoRules(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


class Player:
    def __init__(self):
        self.points = 0

    def add_points(self, choice_points, outcome_points):
        self.points += choice_points + outcome_points


def part_one_rules(lines: list):
    elf_player = Player()
    our_player = Player()

    for line in lines:
        elf_move, my_move = line.split()
        my_move = PartOneRules(my_move).name

        if elf_move == my_move:
            elf_player.add_points(points_dict.get(PartOneRules(elf_move).name), StaticRules.DRAW.value)
            our_player.add_points(points_dict.get(PartOneRules(my_move).name), StaticRules.DRAW.value)

        elif elf_move == PartOneRules.ROCK.value and my_move == PartOneRules.SCISSORS.value:
            elf_player.add_points(points_dict.get(PartOneRules(elf_move).name), StaticRules.WIN.value)
            our_player.add_points(points_dict.get(PartOneRules(my_move).name), StaticRules.LOST.value)

        elif elf_move == PartOneRules.SCISSORS.value and my_move == PartOneRules.ROCK.value:
            elf_player.add_points(points_dict.get(PartOneRules(elf_move).name), StaticRules.LOST.value)
            our_player.add_points(points_dict.get(PartOneRules(my_move).name), StaticRules.WIN.value)

        elif elf_move < my_move:
            elf_player.add_points(points_dict.get(PartOneRules(elf_move).name), StaticRules.LOST.value)
            our_player.add_points(points_dict.get(PartOneRules(my_move).name), StaticRules.WIN.value)

        elif elf_move > my_move:
            elf_player.add_points(points_dict.get(PartOneRules(elf_move).name), StaticRules.WIN.value)
            our_player.add_points(points_dict.get(PartOneRules(my_move).name), StaticRules.LOST.value)

    return our_player.points


def part_two_rules(lines: list):
    elf_player = Player()
    our_player = Player()


    for line in lines:
        elf_move, my_move = line.split()
        my_move = PartTwoRules(my_move).name


        if my_move == PartTwoRules.DRAW.name:
            elf_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.DRAW.value)
            our_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.DRAW.value)

        elif my_move == PartTwoRules.LOSE.name:
            elf_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.WIN.value)
            our_player.add_points(points_dict.get(StaticRules[elf_move].name),StaticRules.LOST.value)

        elif my_move == PartTwoRules.WIN.name:
            elf_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.LOST.value)
            our_player.add_points(points_dict.get(StaticRules[PartTwoRules(elf_move).name].value),
                                  StaticRules.WIN.value)

    return our_player.points


if __name__ == "__main__":
    lines = open_file("puzzle_input.txt")
    my_points_part_one = part_one_rules(lines)
    my_points_part_two = part_two_rules(lines)

    file_path = "Day_2_Answers.json"
    write_answers(2, my_points_part_one, my_points_part_two, file_path)
