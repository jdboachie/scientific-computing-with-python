def parse(problem):
    pieces = problem.split(" ")
    addend, operation, additive = pieces[0], pieces[1], pieces[-1]
    lengths = [len(addend), len(additive)]
    max_length = max(lengths)
    if operation == "+":
        solution = int(addend )+ int(additive)
    elif operation == "-":
        solution = int(addend) - int(additive)
    else:
        raise TypeError("Error: Operator must be '+' or '-'.")

    return addend, operation, additive, max_length, str(solution)

def decorate(problems):
    addends = [x[0] for k,x in problems.items()]
    operations = [x[1] for k,x in problems.items()]
    additives = [x[2] for k,x in problems.items()]
    max_sizes = [x[3] for k, x in problems.items()]
    solutions = [x[-1] for k,x in problems.items()]

    # adding spaces for proper alignment
    for i in range(len(addends)):
        if len(addends[i]) < max_sizes[i]:
            difference = max_sizes[i] - len(addends[i])
            addends[i] = " " * difference + addends[i]

        if len(additives[i]) < max_sizes[i]:
            difference = max_sizes[i] - len(additives[i])
            additives[i] = " " * difference + additives[i]

        if len(solutions[i]) < max_sizes[i] + 2:
            difference = (max_sizes[i] + 2) - len(solutions[i])
            solutions[i] = " " * difference + solutions[i]

    return addends, operations, additives, solutions

def arithmetic_arranger(problems, show_solutions=False):
    arranged_problems = list()
    hash_table = dict()
    for i in range(len(problems)):
        addend, operation, additive, max_length, solution = parse(problems[i])
        hash_table[i] = (addend, operation, additive, max_length, solution)
    decorated = decorate(hash_table)

    addends = decorated[0]
    operations = decorated[1]
    additives = decorated[2]
    addend_string = "  " + ("      ").join(addends)

    # joining the operations
    j = 0
    for i in range(0, len(additives)):
        if i != 0:
            additives[i] = "  " + operations[j] + " " + additives[i]
        else:
            additives[i] = operations[j] + " " + additives[i]
        j += 1

    #creating the underlines
    underlines = []
    for i in range(len(additives)):
        length = len(additives[i])
        if i == 0:
            underlines.append("-" * length)
        else:
            underlines.append("-" * (length - 2))

    additive_string = ("  ").join(additives)
    underline_string = ("    ").join(underlines)

    solutions = decorated[-1]
    solution_string = ("    ").join(solutions)

    arranged_problems = addend_string + "\n" + additive_string + "\n" + underline_string
    if show_solutions:
        arranged_problems += "\n" + solution_string
    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))