from itertools import combinations
import math
# path to the local version of the Advent of Code day 1 input.
path_to_txt_file = 'day1Aoc.txt'

# open local file with Advent of Code day 1 input.
day_1_input = open(path_to_txt_file, 'r')


# reads file and creates a list.
list_of_inputs_as_strs = day_1_input.read().split()

# New list
list_of_inputs_as_ints = []

# This will convert all str to int and append them tho the new list.
for i in list_of_inputs_as_strs:
    list_of_inputs_as_ints.append(int(i))

# print(list_of_inputs_as_ints)

# Check if any of the numbers in the list sum to 2020
def sum_checker(lst):
    """This function will find if any of two numbers of a list sum to 2020"""
    result = []
    sum_found = 0   # Sum of 2020 counter
    while sum_found == 0:
        # Loop through list
        for i in range(0, len(lst)-1):
            # This is the index that will be popped if no other numbers sum 2020
            idx_1 = lst[0]
            idx_to_add = lst[i+1]
            # If we found two numbers that sum 2020
            if idx_1 + idx_to_add == 2020:
                # return the result as a list with the two numbers that sum 2020
                result = [idx_1, idx_to_add]
                # print("We found it.", idx_1, idx_to_add, result)
                # Update counter
                sum_found += 1
                return result
                break

        # If a sum is found return the numbers that were found
        if sum_found == 1:
            # print("found it", result)
            return result
        # Remove the first index and try again. RECURSION
        else:
            # print("try again")
            lst.pop(0)
            # No more numbers to check. Therefore there are no two nums in the list that sum 2020
            if len(lst) == 1:
                # print("Nothing sums to 2020")
                return False
            # RECURSION
            sum_checker(lst)


def sum_checker_3(lst):
    """This function will find 3 numbers that sum to 2020"""
    lst_combo = combinations(lst, 3)    # Creates all possible 3-combinations of all numbers
    for i in lst_combo:     # Iterate through all possible 3-combinations
        if sum(i) == 2020:  # If the sum of a combination is 2020
            return i


# val = sum_checker_3(lst_200)
def product_of_sums(lst):
    """Multiplies the two nums that sum to 2020"""
    return lst[0] * lst[1]


def product_of_sums_3(lst):
    """Multiplies the two nums that sum to 2020"""
    return lst[0] * lst[1] * lst[2]


val_part_2 = sum_checker_3(list_of_inputs_as_ints)
result_1 = math.prod(sum_checker(list_of_inputs_as_ints))
result_2 = math.prod(val_part_2)
print(result_1, result_2)

# day_1_input.readline() # this will read line by line. every execution will read the next line.

# This will close the file.
day_1_input.close()