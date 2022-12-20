from HelperUtils import open_file, write_answers


# 4 chars that are all different signals start of packet
def chars_before_first_packet(packets: list):
    chars = []
    chars_before_start = 0
    for char in packets[0]:
        if len(chars) < 4:
            chars.append(char)
            chars_before_start += 1
        else:
            packet_start = check_unique_chars(chars)

            if packet_start:
                return chars_before_start
            else:
                chars_before_start += 1
                chars.pop(0)
                chars.append(char)

# 14 chars that are all different signals start of packet
def chars_before_first_message(packets: list):
    chars = []
    chars_before_start = 0
    for char in packets[0]:
        if len(chars) < 14:
            chars.append(char)
            chars_before_start += 1
        else:
            packet_start = check_unique_chars(chars)

            if packet_start:
                return chars_before_start
            else:
                chars_before_start += 1
                chars.pop(0)
                chars.append(char)

def check_unique_chars(chars: list):
    if (len(set(chars)) == len(chars)):
        return True
    else:
        return False


if __name__ == "__main__":
    day = 6
    packets = open_file("puzzle_input.txt")
    part_one_ans = chars_before_first_packet(packets)
    part_two_ans = chars_before_first_message(packets)

    file_path = f"Day_{day}_Answers.json"
    write_answers(day, part_one_ans=part_one_ans, part_two_ans=part_two_ans, file_path=file_path)
