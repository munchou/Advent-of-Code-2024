input_file = "AOD-2024-03_input.txt"

# PART 1:
def get_content(chunk):
    content = ""
    if len(chunk) == 2:
        right_part_processed = ""
        left_part = chunk[0]
        left_part = left_part.replace("mul(", "")
        right_part = chunk[1]
        for char in right_part:
            if char == ")":
                break
            right_part_processed += char
            continue        
        try:
            left_part = int(left_part)
            right_part_processed = int(right_part_processed)
            return left_part*right_part_processed
        except ValueError:
            pass
    return 0


def part1(use_read_file):
    result = 0
    if use_read_file == "read":
        with open(input_file, "r") as file:
            user_data = file.read()
    else:
        user_data = use_read_file

    user_data = user_data.replace("mul(","_mul(")
    user_data = user_data.split("_")
    for chunk in user_data:
        if "," in chunk and "mul(" in chunk and ")" in chunk:
            new_chunk = ""
            for char in chunk:
                if char != ")":
                    new_chunk += char
                    continue
                new_chunk += char
                break
            new_chunk = new_chunk.split(",")
            result += get_content(new_chunk)
    
    return result


# PART 2
def part2():
    string_ok = ""
    is_do = True
    with open(input_file, "r") as file:
        user_data = file.read()
        p = 0

        while True:
            if p == len(user_data) - 1:
                string_ok += user_data[p]
                break
            if user_data[p] == "d":
                if user_data[p:p+7] == "don't()":
                    is_do = False
                elif user_data[p:p+4] == "do()":
                    is_do = True
            if is_do:
                string_ok += user_data[p]
            p += 1
        return part1(string_ok)


# RESULT
print("part1:", part1("read")) # 188116424
print("part2:", part2()) # 104245808