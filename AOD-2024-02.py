input_file = "AOD-2024-02_input.txt"


"""The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only
tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe."""

safe_reports = 0


# PART 1:
level_type = ""
def check_type(line):
    if int(line[0]) > int(line[1]):
        line.reverse()
    for h in range(len(line)):
        if h+1 == len(line):
            break
        if int(line[h+1]) > int(line[h]):
            continue
        else:
            return False
    return True

def part1(safe_reports):
    with open(input_file, "r") as file:
        user_data = file.read().split("\n")
        for line in user_data:
            if line:
                line = line.split(" ")
                if check_type(line):
                    r = 0
                    while r+1 != len(line):
                        if 3 >= abs(int(line[r+1]) - int(line[r])) >= 1:
                            if r == len(line)-2:
                                safe_reports += 1
                                r = 0
                                break
                            r += 1
                            continue
                        else:
                            r = 0
                            break
        return safe_reports



# PART 2
test_cases = """48 46 47 49 51 54 56
1 1 2 3 4 5
1 2 3 4 5 5
5 1 2 3 4 5
1 4 3 2 1
1 6 7 8 9
1 2 3 4 3
9 8 7 6 7"""
def part2(safe_reports):    
    with open(input_file, "r") as file:
        user_data = file.read().split("\n")

        user_data = test_cases.split("\n")

        for line in user_data:
            pass
                        
        return safe_reports # not 383

"""
    7 6 4 2 1: Safe without removing any level.
    1 3 2 4 5: Safe by removing the second level, 3.
    1 4 4 6 8: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.
"""

# RESULT
print("part1:", part1(safe_reports)) #321
print("part2:", part2(safe_reports))