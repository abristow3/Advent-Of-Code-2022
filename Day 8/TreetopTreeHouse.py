from HelperUtils import write_answers, open_file

# Each digit is a tree height 0-9 9 being tallest
# Only consider trees in same row and column
# Tree is visible if all trees between it and an edge of grid are shorter
def part_one(grid: list):
    grid
    rows = 0
    columns = 0
    for row in grid:
        print(row)


    print(rows)



if __name__ == "__main__":
    day = 8
    grid = open_file("puzzle_input.txt")

    part_one(grid)

    file_path = f"Day_{day}_Answers.json"
    write_answers(day, part_one_ans=None, part_two_ans=None, file_path=file_path)
