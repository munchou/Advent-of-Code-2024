input_file = "AOD-2024-04_input.txt"

"""Find XMAS or SAMX
function(letter, target) -> ex: function(S, SMAX)
Check:  horizontally -> same line, index + 1-3
        vertically -> next 3 lines, same index
        diagonally -> next 3 lines, index+(1*line number)"""

with open(input_file, "r") as file:
    user_data = file.read()

user_data1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

user_data2 = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""


# PART 1:
def check_horizontally(line, l, target):
    if line[l:l+4] == target:
        return 1
    return 0

def check_vertically(line, line_number, lines, l, target):
    try:
        if f"{line[l]}{lines[line_number+1][l]}{lines[line_number+2][l]}{lines[line_number+3][l]}" == target:
            return 1
    except:
        pass
    return 0

def check_diagonally(line, line_number, lines, l, target):
    result = 0
    if line_number+1 <= len(lines)-3:
        try:
            if f"{line[l]}{lines[line_number+1][l+1]}{lines[line_number+2][l+2]}{lines[line_number+3][l+3]}" == target and l+3 <= len(line) + 1:
                result += 1
        except:
            pass

        try:
            if f"{line[l]}{lines[line_number+1][l-1]}{lines[line_number+2][l-2]}{lines[line_number+3][l-3]}" == target and l-3 >= 0:
                result += 1
        except:
            pass
    return result

def part1(user_data):
    line_number = 0
    result = 0
    lines = [line for line in user_data.split("\n")] # 140 lines in total
    for line in lines:
        for l in range(len(line)):            
            target = "XMAS" if line[l] == "X" else "SAMX" if line[l] == "S" else ""
            result += check_horizontally(line, l, target)
            if line_number+1 <= len(lines)-3:
                result += check_vertically(line, line_number, lines, l, target)
                result += check_diagonally(line, line_number, lines, l, target)
        line_number += 1
    
    return result

user_data2 = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

# PART 2
def part2(user_data):
    pass


# RESULT
print("part1:", part1(user_data)) # 2462
# print("part2:", part2(user_data)) # 