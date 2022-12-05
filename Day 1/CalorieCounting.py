import json
from HelperUtils import open_file, write_answers


def find_highest_calories(lines: list) -> int:
    highest_calories = 0
    calorie_count = 0
    for line in lines:
        if line == "\n":
            if calorie_count > highest_calories:
                highest_calories = calorie_count
            calorie_count = 0
        else:
            calorie_count += int(line)

    return highest_calories


def find_top_three_highest_calories(lines: list) -> int:
    first_highest = 0
    second_highest = 0
    third_highest = 0
    calorie_count = 0

    for line in lines:
        if line == "\n":
            if calorie_count > first_highest:
                third_highest = second_highest
                second_highest = first_highest
                first_highest = calorie_count

            elif calorie_count > second_highest:
                third_highest = second_highest
                second_highest = calorie_count

            elif calorie_count > third_highest:
                third_highest = calorie_count

            calorie_count = 0
        else:
            calorie_count += int(line)

    total_calories = first_highest + second_highest + third_highest
    return total_calories


if __name__ == "__main__":
    elf_calorie_data = open_file("Day 1/puzzle_input.txt")

    highest_cals = find_highest_calories(elf_calorie_data)
    top_three_total_calories = find_top_three_highest_calories(elf_calorie_data)

    file_path = "Day 1/Day_1_Answers.json"
    write_answers(1, highest_cals, top_three_total_calories, file_path)


def part_two_rules(lines: list):
    elf_player = Player()
    our_player = Player()


    for line in lines:
        elf_move, my_move = line.split()
        my_move = PartTwoRules(my_move).name

        print(StaticRules[elf_move].value)

        if my_move == PartTwoRules.DRAW.name:
            elf_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.DRAW.value)
            our_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.DRAW.value)

        elif my_move == PartTwoRules.LOSE.name:
            elf_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.WIN.value)
            our_player.add_points(points_dict.get(StaticRules[elf_move].name),StaticRules.LOST.value)

        elif my_move == PartTwoRules.WIN.name:
            elf_player.add_points(points_dict.get(StaticRules[elf_move].value), StaticRules.LOST.value)
            our_player.add_points(points_dict.get(StaticRules[elf_move].value),StaticRules.WIN.value)

    return our_player.points
