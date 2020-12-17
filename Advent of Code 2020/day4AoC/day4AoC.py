# Make paths
path = 'day4AoCinput.txt'
ex_path = 'example_input.txt'

# Open files
file = open(path, 'r')
ex_file = open(ex_path, 'r')

# This will split by a double line break (\n\n)
# This allows for us to separate the passports to loop through them later
day4AoC_inputs = file.read().split('\n\n')
example_inputs = ex_file.read().split('\n\n')

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
    for passport in list_of_passports:
        print(passport, "\n")
        valid_checker = 0
        for must in must_include:
            if must in passport:
                valid_checker += 1
        if valid_checker == 7:
            valid_passports += 1
        total_passports += 1
    return total_passports, valid_passports

ex_total, ex_valid = valid_passport_counter(example_inputs)
day4_total, day4_valid = valid_passport_counter(day4AoC_inputs)

print("EXAMPLE SOLUTION:\nThere are a total of " + str(ex_total) + " passports,\nand there are " + str(ex_valid) + " valid passports.")
print("EXAMPLE SOLUTION:\nThere are a total of " + str(day4_total) + " passports,\nand there are " + str(day4_valid) + " valid passports.")



