import re

# Make paths
path = 'day4AoCinput.txt'
ex_path = 'example_input.txt'

# Opens the inputs for day 4 Advent of Code
with open(path, 'r') as file:
    day4AoC_inputs = file.read().split('\n\n')
# Opens example inputs.
with open(ex_path, 'r') as file:
    example_inputs = file.read().split('\n\n')

def valid_passport_counter(list_of_passports):
    """This function will count the total number of passports and valid passports.

    A valid passport must include everything in the must_include list below.
    the country id is missing from the must_include list because it is not required
    to be a valid passport.

    The for loop, loops through all the passports and for every passport a new loop goes loops through
    the must_include list and checks if each field is in the passport. If it is we update the valid checker by 1.
    If the valid checker equals 7, the number of fields that must be on a passport to consider it valid, then that
    passport is valid and we update the valid_passport counter by 1.
    """
    # A valid passport must include all of these fields to be considered valid.
    must_include = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    total_passports = 0
    valid_passports = 0
    has_required_fields = []
    for passport in list_of_passports:
        # print(passport, "\n")
        valid_checker = 0
        for must in must_include:
            if must in passport:
                valid_checker += 1
        if valid_checker == 7:
            valid_passports += 1
            has_required_fields.append(passport)
        total_passports += 1
    return total_passports, valid_passports, has_required_fields

ex_total, ex_valid, ex_has_required_fields = valid_passport_counter(example_inputs)
day4_total, day4_valid, day4_has_required_fields = valid_passport_counter(day4AoC_inputs)

# print("EXAMPLE SOLUTION:\nThere are a total of " + str(ex_total) + " passports,\nand there are " + str(ex_valid) + " valid passports.")
# print("EXAMPLE SOLUTION:\nThere are a total of " + str(day4_total) + " passports,\nand there are " + str(day4_valid) + " valid passports.")



def valid_check(passport_list):
    """This function will check if the fields of a passport are valid.

    This function takes the list from part 1. This list is a list of passports that will have all required fields.

    All the continue statements are for when something is found to be either true or false,
    then it goes to the next loop, so it does not go to the next if statements.

    If a field is found false the invalid counter is incremented by 1 and continued to the next iteration.
    Check if the invalid_counter is greater than 0, which it is because a field was false, then break out of the fields
    loop and go the next passport and loop through the fields.
    """

    # Keep track of the passports with all valid fields.
    valid_counter = 0
    for passport in passport_list:
        # This will split the passports into their respective fields
        passport_list = passport.split()
        # This will keep track if something is invalid
        invalid_counter = 0
        # Loop through the fields
        for field in passport_list:
            # If one field is found invalid then the whole passport is invalid.
            if invalid_counter > 0:
                break
            # Split the field and value_of_field to make it easy to check the different values.
            field, value_of_field = field.split(':')
            # Check if birth year is at least 1920 and at most 2002
            if field == 'byr':
                byr_as_int = int(value_of_field)
                if 1920 <= byr_as_int <= 2002:
                    continue
                else:
                    invalid_counter += 1
                    continue
            # Check if issue year is at least 2010 and at most 2020
            if field == 'iyr':
                iyr_as_int = int(value_of_field)
                if 2010 <= iyr_as_int <= 2020:
                    continue
                else:
                    invalid_counter += 1
                    continue
            # Check if expiration date is at least 2020 and at most 2030
            if field == 'eyr':
                eyr_as_int = int(value_of_field)
                if 2020 <= eyr_as_int <= 2030:
                    continue
                else:
                    invalid_counter += 1
                    continue
            # Check the last to elements and they need to equal cm or in
            if field == 'hgt':
                in_or_cm = value_of_field[-2:]
                value = value_of_field.split(in_or_cm)[0]
                if in_or_cm == "in":
                    if 59 <= int(value) <= 76:
                        continue
                    else:
                        invalid_counter += 1
                        continue
                if in_or_cm == "cm":
                    if 150 <= int(value) <= 193:
                        continue
                    else:
                        invalid_counter += 1
                        continue
                else:
                    invalid_counter += 1
                    continue
            # Check if the value begins with # and has exactly 6 characters following that are either 0-9 or a-f
            if field == 'hcl':
                # first char is # followed by exactly 6 chars that must be 0-9 or a-f
                regex_expression = re.compile('^[#][0-9a-f]{6}$')
                if regex_expression.findall(value_of_field):
                    continue
                else:
                    invalid_counter += 1
                    continue
            # Check if the eye color is one of the valid eye colors.
            if field == 'ecl':
                # Valid eye colors for the eye color fields.
                valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if value_of_field in valid_eye_color:
                    continue
                else:
                    invalid_counter += 1
                    continue
            # Check for 9 digits in the range 000000000 to 999999999
            if field == 'pid':
                # ^ indicates beginning of string
                # \d indicates any digit 0-9
                # {9} indicates it is checking for 9 consecutive digits
                # $ indicates the end of a string
                expression = re.compile('^\d{9}$')
                # This will check the value fo the PID to the regex.
                if expression.findall(value_of_field):
                    continue
                else:
                    invalid_counter += 1
                    continue
            if field == 'cid':
                continue

        # Once all loops have been looped through then check if
        # the invalid counter is 0.
        if invalid_counter == 0:
            # The passport has all fields valid
            valid_counter += 1

    # print(valid_counter)
    return valid_counter

print(valid_check(day4_has_required_fields))
