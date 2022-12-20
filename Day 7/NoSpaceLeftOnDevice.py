from HelperUtils import open_file, write_answers

def sum_of_dir_sizes(log: list):
    dirs = {"/home": 0}
    path = "/home"

    # Process every command
    for command in log:

        # Commands that start with $
        if command[0] == "$":

            # Do nothing
            if command[2:4] == "ls":
                pass

            # Manage changing the path
            elif command[2:4] == "cd":

                # # Go back to the root
                if command[5:6] == "/":
                    path = "/home"

                # Go back in the path
                elif command[5:7] == "..":
                    path = path[0:path.rfind("/")]

                # Change the path
                else:
                    dir_name = command[5:]  # Get name of directory
                    path = path + "/" + dir_name  # Add to the path
                    dirs.update({path: 0})  # Update our dictionary


        # Do nothing when listing directories available
        elif command[0:3] == "dir":
            pass

        else:
            size = int(command[:command.find(" ")])  # Get size of file

            # Update size for every directory down to /home
            dir = path
            for i in range(path.count("/")):
                dirs[dir] += size
                dir = dir[:dir.rfind("/")]

    total = 0

    # space required - space unused (total space - space used)
    limit = 30000000 - (70000000 - dirs["/home"])
    valid_dirs = []

    # Iterate through every path
    for dir in dirs:

        # part 1
        if dirs[dir] < 100000:
            total += dirs[dir]

        # part 2
        if limit <= dirs[dir]:
            valid_dirs.append(dirs[dir])

    smallest = min(valid_dirs)

    return total, smallest


if __name__ == "__main__":
    day = 7
    log = open_file("puzzle_input.txt")

    part_one_ans, part_two_ans = sum_of_dir_sizes(log)

    file_path = f"Day_{day}_Answers.json"
    write_answers(day, part_one_ans=part_one_ans, part_two_ans=part_two_ans, file_path=file_path)
