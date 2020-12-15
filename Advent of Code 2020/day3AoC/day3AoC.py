path = 'day3AoCinput.txt'
file = open(path, 'r')

day3_inputs = file.read().splitlines()
example_inputs = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.', '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']

def extender(list_input):
    """This function will take a list as an input
    that is displayed as the local geology.

    First we find out how many times to repeat the local geology. Must be an integer.

    Create new list that the extended geology will be appended.

    """
    times_to_repeat = (int(len(list_input)/3))
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


example = extender(day3_inputs)
ex_space, ex_tree = check_for_space_or_tree(example)

print("Spaces hit: " + str(ex_space), "\nTrees hit: " + str(ex_tree))