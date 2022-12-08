from HelperUtils import open_file, write_answers


def total_fully_overlapped_pairs(assignments: list):
    overlapped_pairs = 0

    for pair in assignments:
        pair = pair.strip()

        # Split string on comma which separates pairs. Store each range in new var
        assignment_one, assignment_two = pair.split(",")

        # Split each assignment range into upper and lower bound
        assignment_one_lower, assignment_one_upper = assignment_one.split("-")
        assignment_two_lower, assignment_two_upper = assignment_two.split("-")

        if int(assignment_two_lower) in range(int(assignment_one_lower), int(assignment_one_upper) + 1) and \
                int(assignment_two_upper) in range(int(assignment_one_lower), int(assignment_one_upper) + 1):
            overlapped_pairs += 1

        elif int(assignment_one_lower) in range(int(assignment_two_lower), int(assignment_two_upper) + 1) and \
                int(assignment_one_upper) in range(int(assignment_two_lower), int(assignment_two_upper) + 1):
            overlapped_pairs += 1

    return overlapped_pairs


def total_overlapped_pairs(assignments: list):
    overlapped_pairs = 0

    for pair in assignments:
        pair = pair.strip()

        # Split string on comma which separates pairs. Store each range in new var
        assignment_one, assignment_two = pair.split(",")

        # Split each assignment range into upper and lower bound
        assignment_one_lower, assignment_one_upper = assignment_one.split("-")
        assignment_two_lower, assignment_two_upper = assignment_two.split("-")

        if int(assignment_two_lower) in range(int(assignment_one_lower), int(assignment_one_upper) + 1) or \
                int(assignment_two_upper) in range(int(assignment_one_lower), int(assignment_one_upper) + 1):
            overlapped_pairs += 1

        elif int(assignment_one_lower) in range(int(assignment_two_lower), int(assignment_two_upper) + 1) or \
                int(assignment_one_upper) in range(int(assignment_two_lower), int(assignment_two_upper) + 1):
            overlapped_pairs += 1

    return overlapped_pairs


if __name__ == "__main__":
    assignments = open_file("puzzle_input.txt")
    part_one_answer = total_fully_overlapped_pairs(assignments)
    part_two_answer = total_overlapped_pairs(assignments)

    file_path = "Day_4_Answers.json"
    write_answers(4, part_one_ans=part_one_answer, part_two_ans=part_two_answer,file_path=file_path)
