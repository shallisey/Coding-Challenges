# path to text file to be opened
path = 'day2AoCinput.txt'
# open file
file = open(path, 'r')
# Make list all off inputs for Day 2 of Adevent of Code.
day2AoC_inputs = file.read().splitlines()




#####################################################################
################### DAY 2 PART 1 ####################################
#####################################################################
def password_validator(input_list):
    """This function will return all valid passwords that have the correct number
    of number of specified letters.
    """
    valid_passwords = 0
    for line in input_list:
        # Create list of each string separated by a space.
        # ['1-3', 'a:', 'abcde']
        words = line.split()
        # First part is then separated by the - character.
        # The range
        # Left side is the low, and the right side is the high input.
        low, high = words[0].split('-')
        # Assign the first character of the [1] list element
        # This is the what we are checking
        validator = words[1][0]
        # Assign the [2] element as the given password.
        given_password = words[2]

        letter_count = 0
        # Loop through the password given
        for char in given_password:
            # For every character that equals the validator
            if char == validator:
                # update count
                letter_count += 1
        # Check if letter count is within the range
        if int(low) <= letter_count <= int(high):
            # Update valid password count.
            valid_passwords += 1
    return valid_passwords



#####################################################################
################### DAY 2 PART 2 ####################################
#####################################################################


def position_check(input_list):
    valid_counter = 0
    for line in input_list:
        # Create list of each string separated by a space.
        # ['1-3', 'a:', 'abcde']
        words = line.split()
        # First part is then separated by the - character.
        # Left side is the low, and the right side is the high input.
        first_position, second_position = words[0].split('-')
        # Assign the first character of the [1] list element
        # This is the what we are checking
        validator = words[1][0]
        # Assign the [2] element as the given password.
        given_password = words[2]

        # Check if the both positions have the validator
        if validator == given_password[int(first_position) - 1] and validator == given_password[int(second_position) - 1]:
            # print("Invalid because both position " + first_position \
            #       + " and position " + second_position \
            #       + " contain " + validator + ".")
            valid_counter = valid_counter
        # Check if neither positions have the validator
        elif validator != given_password[int(first_position) - 1] and validator != given_password[int(second_position) - 1]:
            # print("Invalid because neither position " + first_position \
            #       + " nor position " + second_position \
            #       + " contains " + validator + ".")
            valid_counter = valid_counter
        # Check if the first position has the validator and the second position does not.
        elif validator == given_password[int(first_position) - 1] and validator != given_password[int(second_position) - 1]:
            # print("First position correct.")
            # Update the valid counter
            valid_counter += 1
        # Check if the first position does not have the validator and the second position does have the validator.
        elif validator != given_password[int(first_position) - 1] and validator == given_password[int(second_position) - 1]:
            # print("Second position correct")
            # Update valid counter
            valid_counter += 1
    return valid_counter


example_inputs = ['1-3 a: abcde', '1-3 c: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']


ex_password = password_validator(example_inputs)
day2AoCP1_answer = password_validator(day2AoC_inputs)

ex_position = position_check(example_inputs)
day2AoCP2_answer = position_check(day2AoC_inputs)
print(day2AoCP1_answer, day2AoCP2_answer)
