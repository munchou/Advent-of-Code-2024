input_file = "AOD-2024-01_input.txt"

final_sum = 0

list1 = []
list2 = []

with open(input_file, "r") as file:
    user_data = file.read()
    user_data = user_data.split("\n")
    for i in user_data:
        i = i.split("  ")
        list1.append(int(i[0]))
        list2.append(int(i[1]))

list1, list2 = sorted(list1), sorted(list2)

# PART 1:
def part1(final_sum = 0):
    for n in range(len(list1)):
        final_sum += abs(list1[n] - list2[n])
    return final_sum


# PART 2
def part2(final_sum = 0):
    list1_cleaned = [num for num in list1 if num in list2]
    for num in list1_cleaned:
        final_sum += num * list2.count(num)
    return final_sum

# RESULT
print("part1:", part1(final_sum))
print("part2:", part2(final_sum))