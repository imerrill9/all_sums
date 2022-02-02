def main():
    print(
        """
************************************************************************************
This program calculates all the possible combinations of summations to find a value.
          
Enter a number:
        """
    )

    while True:
        entered = input()
        if entered.isnumeric():
            solutions = find_combinations(int(entered))
            print(
                f"""
***********************************************************************************
All possible combinations that add up to {entered}:
 
                   """
            )
            display(solutions)
            quit()
        elif entered == "exit":
            quit()
        else:
            print(f"{entered} is not an integer, please enter an integer:")


def find_combinations(target_value):
    solutions = set()
    for i in range(1, target_value):  # run recursion starting at every value less than target
        solutions.update(find_combinations_given_start(i, target_value, [], set()))
    return solutions


def find_combinations_given_start(current_value, target_value, combination, solutions):
    if tuple(sorted(combination)) in solutions or sum(combination) > target_value:  # prune
        return solutions
    elif sum(combination) == target_value:  # add found solution to solutions
        # uncomment to watch for values that are too large for this solution ( >18 lol XD)
        # print(f"Solution found! {combination}")
        solutions.add(tuple(sorted(combination)))
        return solutions
    else:
        # branch 1 (Add more of the current value)
        branch_one = combination.copy()
        branch_one.append(current_value)
        solutions.update(find_combinations_given_start(current_value, target_value, branch_one, solutions))

        # branch 2 (Add every possible value less than the target)
        branch_two = combination.copy()
        for coin in range(1, target_value):
            branch_two.append(coin)
            solutions.update(find_combinations_given_start(current_value, target_value, branch_two, solutions))

        return solutions


def display(solutions):
    for solution in solutions:
        print(solution)


# prevents script from running if it's imported
if __name__ == "__main__":
    main()
