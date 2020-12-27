# Paths to files
path = 'day5AoCinput.txt'
ex_path = 'example.txt'

# Open files
with open(path, 'r') as file:
    day5AoC_inputs = file.read().splitlines()

with open(ex_path, 'r') as ex_file:
    example_inputs = ex_file.read().splitlines()


#######PART 1##########
def boarding_pass(lst_of_passes):
    """This function will return the max seat ID from a list of boarding passes.

    The formula for a seat ID is multiply the row by 8, then add the column. (row*8+column)

    Binary search to find rows and columns
    """
    list_of_seat_ID = []
    # Loop through all boarding passes
    for b_pass in lst_of_passes:
        # Use list comprehension to create a list with all the rows from 0-127
        rows = [row for row in range(128)]
        # Use list comprehension to create a list with all the columns from 0-8
        columns = [col for col in range(8)]
        # Gives us the first 7 characters from a boarding pass.
        seat_row = b_pass[0:7]
        # Gives us the final 3 characters from a boarding pass.
        seat_columns = b_pass[-3:]

        # Loop through the first 7 characters of the boarding pass.
        for row in seat_row:
            # "F" is the lower half
            if row == "F":
                rows = rows[:len(rows)//2]
            # "B" is the upper half
            if row == "B":
                rows = rows[len(rows)//2:]
        # Loop through the final 3 characters of the boarding pass.
        for col in seat_columns:
            # "L" is the lower half
            if col == "L":
                columns = columns[:len(columns)//2]
            # "R" is the upper half.
            if col == "R":
                columns = columns[len(columns)//2:]
        # Formula to give the seat ID
        seat_ID = rows[0] * 8 + columns[0]
        # add seat_ID to list of seat_ID
        list_of_seat_ID.append(seat_ID)
        # print("Rows: " + str(rows[0]) + ", ", "Columns: " + str(columns[0]) + ", ", "seat ID: " + str(seat_ID))
    # Max seat ID of all the seat ID's
    max_seat_ID = max(list_of_seat_ID)
    return list_of_seat_ID, max_seat_ID


list_of_seat_ID, solution = boarding_pass(day5AoC_inputs)

#######PART 2##########

def open_seat(all_seat_ID):
    """This function will return the open seat that has not been taken yet."""
    open_seat = []
    # Loop through all seat IDs starting with 38, min seat ID, and 998, the max seat ID.
    for seat in range(38, len(all_seat_ID)):
        # If a seat is not in the all_seat_ID list then that is the open seat.
        if seat not in all_seat_ID:
            open_seat.append(seat)
    return open_seat

print(open_seat(list_of_seat_ID))