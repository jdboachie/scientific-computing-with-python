import re


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

        if len(str(solutions[i])) < max_sizes[i] + 2:
            difference = (max_sizes[i] + 2) - len(str(solutions[i]))
            solutions[i] = " " * difference + str(solutions[i])

    return addends, operations, additives, solutions


def arithmetic_arranger(problems, show_solutions=False):

    # Checking for more than 5 problems in the problem set
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = list()
    hash_table = dict()

    for i in range(len(problems)):
        pieces = problems[i].split(" ")
        addend, operation, additive = pieces[0], pieces[1], pieces[-1]
        lengths = [len(addend), len(additive)]
        max_length = max(lengths)

        search_addend = re.findall("((?![0-9]).)", addend)
        search_additive = re.findall("((?![0-9]).)", additive)

        # Checking that operands only contain digits
        if ((len(search_addend) == 1) and (len(search_addend[0]) != 0)):
            return "Error: Numbers must only contain digits."

        elif ((len(search_additive) == 1) and (len(search_additive[0]) != 0)):
            return "Error: Numbers must only contain digits."

        # Validating operation type and operand lengths
        if operation == "+":
            solution = int(addend) + int(additive)
        elif operation == "-":
            solution = int(addend) - int(additive)
        else:
            return "Error: Operator must be '+' or '-'."

        if (int(addend) > 9999) or (int(additive) > 9999):
            return "Error: Numbers cannot be more than four digits."


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

    # creating the underlines
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

    # Constructing the output format
    arranged_problems = addend_string + "\n" + additive_string + "\n" + underline_string
    if show_solutions:
        arranged_problems += "\n" + solution_string
    return arranged_problems