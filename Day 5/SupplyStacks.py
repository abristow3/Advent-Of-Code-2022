from HelperUtils import open_file, write_answers


def rearrange_crates(current_crate_layout, instructions):
    pass


def setup_bins(num_bins: int):
    crate_bins = {}
    for crate_bin in range(num_bins):
        crate_bins[crate_bin + 1] = []
    return crate_bins


def clean_file(crates):
    for index, line in enumerate(crates):
        crates[index] = line.replace("\n", "")

    return crates


def build_crate_layout(crates):
    index, num_bins = 0, 0
    i, j, k = 0, 2, 4

    for index, line in enumerate(crates):
        if "1" in line:
            print("End of crate layout found. Arranging crates.")
            # Remove white space and see how many bins to make by len()
            line = line.replace(" ", "")
            num_bins = len(line)
            break

    # Now we enumerate backwards to build crate layout for bins
    # You can tell which crate goes in which bin by checking every 4
    # chars per line. chars 0-3 are bin 1, 4-7 are bin 2, etc

    # Delete all index after our bins from file
    del crates[index:]
    crate_bins = setup_bins(num_bins)

    for line in reversed(list(enumerate(crates))):
        line = line[1]
        bins_to_fill = (len(line) + 1) // 4

        for crate_bin in range(bins_to_fill):
            crate_bin += 1

            if line[i] == "[" and line[j] == "]":
                crate_bins[crate_bin].append(line[:k])

            line = line[k:]

    return crate_bins


def arrange_crates(crate_bins, crates):
    for index, line in enumerate(crates):
        if "move" in line:
            # Get digits out of string
            res = [int(i) for i in line.split() if i.isdigit()]

            num_to_move, start_bin, end_bin = res

            while num_to_move != 0:
                temp = crate_bins[start_bin].pop()
                crate_bins[end_bin].append(temp)

                num_to_move -= 1

    top_items = ""
    for crate in crate_bins.values():
        top_items += crate.pop()

    top_items = top_items.replace("[", "").replace("]", "").replace(" ", "")

    return top_items


def arrange_crates_part_two(crate_bins, crates):
    for index, line in enumerate(crates):
        if "move" in line:
            # Get digits out of string
            res = [int(i) for i in line.split() if i.isdigit()]

            # Set rules
            num_to_move, start_bin, end_bin = res

            # Slice start bin for # of crates to move and keep order
            temp = crate_bins[start_bin][-num_to_move:]

            # Remove those crates from start bin
            del crate_bins[start_bin][-num_to_move:]

            # Reverse the list so we can pop and append while keeping order
            temp.reverse()

            # Iterate over temp and pop each index from list and add to end bin
            for _ in range(len(temp)):
                crate_bins[end_bin].append(temp.pop())

    top_items = ""
    for crate in crate_bins.values():
        top_items += crate.pop()

    top_items = top_items.replace("[", "").replace("]", "").replace(" ", "")

    return top_items


if __name__ == "__main__":

    # Too lazy to clean this up to remove repitive calls
    crates = open_file("puzzle_input.txt")
    crates = clean_file(crates)
    crate_bins = build_crate_layout(crates)

    crates = open_file("puzzle_input.txt")
    crates = clean_file(crates)

    part_one_ans = arrange_crates(crate_bins, crates)

    crates = open_file("puzzle_input.txt")
    crates = clean_file(crates)
    crate_bins = build_crate_layout(crates)

    crates = open_file("puzzle_input.txt")
    crates = clean_file(crates)

    part_two_ans = arrange_crates_part_two(crate_bins, crates)

    file_path = "Day_5_Answers.json"
    write_answers(5, part_one_ans=part_one_ans, part_two_ans=part_two_ans, file_path=file_path)
