from HelperUtils import open_file, write_answers


def rearrange_crates(current_crate_layout, instructions):
    pass


def get_crate_layout(crates):
    for index, line in enumerate(crates):
        crates[index] = line.replace(" ", ",")

    return crates


if __name__ == "__main__":
    crates = open_file("puzzle_input.txt")
    crates = get_crate_layout(crates)
    print(crates)

    file_path = "Day_4_Answers.json"
    write_answers(5, part_one_ans=None, part_two_ans=None, file_path=file_path)
