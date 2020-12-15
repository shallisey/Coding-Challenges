path = 'day3AoCinput.txt'
file = open(path, 'r')

day3_inputs = file.read().splitlines()
example_inputs = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.', '..#.##.....',
                  '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']

#####PART 1######


def extender(list_input, position_to_right):
    """This function will take a list as an input
    that is displayed as the local geology.

    First we find out how many times to repeat the local geology. Must be an integer.

    Create new list that the extended geology will be appended.

    """
    # times_to_repeat = (int(len(list_input) / position_to_right))
    times_to_repeat = 100
    print(times_to_repeat)
    extended_list = []
    for line in list_input:
        extend = line * times_to_repeat
        extended_list.append(extend)
    return extended_list


def check_for_space_or_tree(extender_list):
    """This function takes the extended geology list from the extender function


    """
    tree_counter = 0
    space_counter = 0
    position_to_move = 0

    new_list = ""
    for i in extender_list:
        s = list(i)
        if s[position_to_move] == ".":
            s[position_to_move] = "O"
            space_counter += 1
        else:
            s[position_to_move] = "X"
            tree_counter += 1
        position_to_move += 3
        print(new_list.join(s))
    return space_counter, tree_counter


# example = extender(day3_inputs, 3)
# ex_space, ex_tree = check_for_space_or_tree(example)
#
# print("Spaces hit: " + str(ex_space), "\nTrees hit: " + str(ex_tree))

#######Part 2##########

def slope_checker(input_list, position_to_right, position_down):
    """This function will check how many trees are hit with a certain slope.

    The function will take three inputs.
    The list to input.
    The position movement to the right for the slope.
    The position movement down for the slope.

    First I moved the extender inside this function
    just so I don't have to make a separate function call.



    """

    # Create new list the extends the 'geology' a certain number of times.
    times_to_repeat = 100
    extended_list = []  # This is the new extended geology
    for line in input_list:
        extend = line * times_to_repeat
        extended_list.append(extend)

    tree_counter = 0
    position_to_move = 0    # This is used later. It will determine the slope in which we are moving

    new_list = ""   # We need to create a new list as a string so we can update the X's and O's.
    count = 0   # This determines the position down
    for line in extended_list:
        s = list(line)  # The line is stored as a list
        # Position down
        if count % position_down != 0:  # This determines the down position for the slope.
            count += 1  # This gives the down movement for the next iteration
            print(new_list.join(s))     # Print the entire line
            continue
        if s[position_to_move] == ".":  # If it is a space
            s[position_to_move] = "O"   # Update the space as O
        else:
            s[position_to_move] = "X"   # If it is a tree
            tree_counter += 1           # Update the tree as X
        position_to_move += position_to_right   # This will give us the right movement for the next iteration.
        count += 1 # This gives the down movement for the next iteration
        print(new_list.join(s))     # Print the line with the updated X or O
    return tree_counter     # Return tree_counter.



r1d1solution = slope_checker(day3_inputs, 1, 1)
r3d1solution = slope_checker(day3_inputs, 3, 1)
r5d1solution = slope_checker(day3_inputs, 5, 1)
r7d1solution = slope_checker(day3_inputs, 7, 1)
r1d2solution = slope_checker(day3_inputs, 1, 2)
print(r1d1solution * r3d1solution * r5d1solution * r7d1solution * r1d2solution)







