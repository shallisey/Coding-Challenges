path = 'day6AoCinput.txt'
ex_path = 'example_input.txt'

with open(path, 'r') as file:
    day6AoC_inputs = file.read().split('\n\n')

with open(ex_path, 'r') as file:
    ex_inputs = file.read().split('\n\n')


##############Part 1###############


def yes_answers_non_repeating(lst_of_inputs):
    """This function will return a list of the answers non repeating
    from each group."""
    # All non repeating answers initialize
    yes_answers = []
    # Loop through all groups.
    for groups in lst_of_inputs:
        # Non repeating answers per group initialize
        non_repeating_list = []
        # Loop through each answer from a specific group
        for individual_answer in groups:
            # \n does count for anything. This just gets rid of any \n that snuck through
            if individual_answer == '\n':
                continue
            # If an answer is not in the non_repeating answers.
            if individual_answer not in non_repeating_list:
                # Add it to the list
                non_repeating_list.append(individual_answer)
        # Add the non repeating answers from single group to all non repeating answers list.
        yes_answers.append(non_repeating_list)
    return yes_answers

# All non repeating answers for each group as they appeared.
yes_answers = yes_answers_non_repeating(day6AoC_inputs)

# Creates dictionary where the key=group number, and value=All none repeating yes answers for the group
answer_list = dict(zip(range(1, len(day6AoC_inputs) + 1), yes_answers))

def sum_of_answers(dict_of_answers):
    """This function returns the sum of the total number of yes answers."""
    sum_of_answers = 0
    # Loop through the all groups
    for key in dict_of_answers:
        # Add the length of the yes_answers list to the sum_of_answers
        sum_of_answers += len(dict_of_answers[key])
    return sum_of_answers


##############Part 2###############


def answers_all_persons_answered(lst_of_inputs):
    """This function returns the sum of all answers in which everyone in a group answered yes.."""
    # Store the answers that were shared in a group
    yes_answers = []
    # Loop through all groups
    for group in lst_of_inputs:
        # persons is really just the group but in a list so it is easier use the data
        persons = group.split('\n')
        # This is the first persons answers
        # This the standard for all answers to be checked
        check = set(persons[0])
        # Loop through all individual persons answer starting from the 2nd/1st element of the list
        for individual in range(1, len(persons)):
            # Bitwise operator to add all answers that equal the check
            check &= set(persons[individual])
        # If any answer is yes through all persons then update yes answers
        yes_answers.append(len(check))
    result = sum(yes_answers)
    return result


sum_of_part_1 = sum_of_answers(answer_list)
print('The sum of the part 1 is: ' + str(sum_of_part_1))

sum_answers = answers_all_persons_answered(day6AoC_inputs)
print("The sum of part 2 is: " + str(sum_answers))
