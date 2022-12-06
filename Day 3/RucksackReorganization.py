from HelperUtils import open_file, write_answers


# Rucksack has 2 comppartments
# all items of given type go into exactly 1 of the 2 compartments
# one item type per rucksack is messed up
# item type is determined by letter and case: a and A are different

# list of items in each rucksack is given as characters on a single line
# rucksack compartments each have the same # of items
# First half of characters is compartment 1, second half is compartment 2
# a-z is priority 1-26, A-Z is priority 27-52
# Find sum of priorities of item type that appears in both compartments

def rucksack_reorganization_part_one(rucksacks: list):
    priority_sum = 0

    for rucksack in rucksacks:
        # Remove whitespace and \n from strings
        rucksack = rucksack.strip()
        compartment_one, compartment_two = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]

        # Find common item between 2 lists and pop it from set
        common_item = (set(compartment_one) & set(compartment_two)).pop()

        # If the char is upper case, get ascii value and sub by 38
        # to start at end of lowercase ascii values
        if common_item.isupper():
            priority_sum += ord(common_item) - 38

        # Else sub by 96 to get lowercase ascii value starting at 1
        else:
            priority_sum += ord(common_item) - 96

    return priority_sum


def rucksack_reorganization_part_two(rucksacks: list):
    # elfs in 3 groups, each carry badge that identifies group item type
    # at most 2 elves in the group of 3 will be carrying any other item type
    priority_sum = 0
    counter = 0
    group_of_three = {"Elf 1": [], "Elf 2": [], "Elf 3": []}

    for rucksack in rucksacks:
        counter += 1
        # Remove whitespace and \n from strings
        rucksack = rucksack.strip()

        if counter < 3:
            # unpack string into list and assign to key
            group_of_three[f"Elf {counter}"] = [*rucksack]
        elif counter == 3:
            group_of_three[f"Elf {counter}"] = [*rucksack]
            # Find common item between 3 lists and pop it from set
            common_item = (set(group_of_three["Elf 1"]) & set(group_of_three["Elf 2"]) & set(
                group_of_three["Elf 3"])).pop()

            # If the char is upper case, get ascii value and sub by 38
            # to start at end of lowercase ascii values
            if common_item.isupper():
                priority_sum += ord(common_item) - 38

            # Else sub by 96 to get lowercase ascii value starting at 1
            else:
                priority_sum += ord(common_item) - 96

            # Reset lists to empty
            group_of_three = {"Elf 1": [], "Elf 2": [], "Elf 3": []}
            counter = 0

    return priority_sum


if __name__ == "__main__":
    rucksacks = open_file("puzzle_input.txt")
    priority_sum_part_one = rucksack_reorganization_part_one(rucksacks)
    priority_sum_part_two = rucksack_reorganization_part_two(rucksacks)

    file_path = "Day_3_Answers.json"
    write_answers(3, priority_sum_part_one, priority_sum_part_two, file_path)


