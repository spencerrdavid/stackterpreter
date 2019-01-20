import sys

def load_file(file):
    print('Reading file...')
    in_file = open(file, 'r')
    lines = in_file.readlines()
    instructions = []
    for line in lines:
        words = line.split(" ")
        element = []
        for word in words:
            element.append(word.strip())
        instructions.append(element)
    # print(instructions)
    return instructions

def interpret(instructions):
    stack = []
    pc = 0
    while(pc < len(instructions)):
        instru = instructions[pc]
        if instru[0] == "INT":
            # push integer onto stack
            stack.append(int(instru[1]))
        elif instru[0] == "ADD":
            # add top two integers
            op1 = stack[len(stack) - 2]
            op2 = stack[len(stack) - 1]
            result = op1 + op2
            # pop operands and append result
            stack.remove(stack[len(stack) - 2])
            stack.remove(stack[len(stack) - 1])
            stack.append(result)
        elif instru[0] == "SUB":
            # subtract top integer from next integer
            op1 = stack[len(stack) - 2]
            op2 = stack[len(stack) - 1]
            result = op1 - op2
            # pop operands and append result
            stack.remove(stack[len(stack) - 2])
            stack.remove(stack[len(stack) - 1])
            stack.append(result)
        elif instru[0] == "JGE":
            top = stack[len(stack) - 1]
            if top >= 0:
                # jump to instruction at instru[1]
                pc = int(instru[1])
                continue
        elif instru[0] == "PRINT":
            print(stack[len(stack) - 1])
        pc += 1
    return stack

instructions = load_file(sys.argv[1])
result = interpret(instructions)
print('Stack:')
print(result)
