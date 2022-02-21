import enum
import math

# opcodes = enum.Enum('opcodes', 'PLUS MINUS TIMES DIVIDE DUP NOP')
opcodes = enum.Enum('opcodes', 'PLUS MINUS TIMES DIVIDE DUP SWAP')  # MOD = DUP


def eval(stack, program):
    while program:
        op = program[0]
        program = program[1:]
        if op == opcodes.PLUS:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2)
        elif op == opcodes.MINUS:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 - op2)
        elif op == opcodes.TIMES:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 * op2)
        elif op == opcodes.DIVIDE:
            op1 = stack.pop()
            op2 = stack.pop()
            try:
                stack.append(op1 / op2)
            except Exception:
                return math.inf
        elif op == opcodes.SWAP:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            stack.append(tmp1)
            stack.append(tmp2)
        elif op == opcodes.DUP:
            tmp = stack.pop()
            stack.append(tmp)
            stack.append(tmp)
        else:
            stack.append(op)
    return stack.pop()


def make_function(program):
    """
    Function that takes a program as input and returns a function that perform the described program
    :param program: program considered
    :return: function that emulates the program
    """

    def function_from_prgr(x, program=program):
        # stack = [0, 0] + x  # adding [0, 0] to make compilable all the programs as [opcodes.MINUS]
        stack = x  # adding [0, 0] to make compilable all the programs as [opcodes.MINUS]

        if type(stack) is not list:
            stack = stack.tolist()
        while program:
            op = program[0]
            program = program[1:]
            if op == opcodes.PLUS:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 + op2)
            elif op == opcodes.MINUS:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 - op2)
            elif op == opcodes.TIMES:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 * op2)
            elif op == opcodes.DIVIDE:
                op1 = stack.pop()
                op2 = stack.pop()
                try:
                    stack.append(op1 / op2)
                except Exception:
                    return math.inf
            elif op == opcodes.SWAP:
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp1)
                stack.append(tmp2)
            elif op == opcodes.DUP:
                tmp = stack.pop()
                stack.append(tmp)
                stack.append(tmp)
            else:
                stack.append(op)
        if stack:
            return stack.pop()  # in the last value of the stack is collected the value of the fitness
        else:
            return 10*+6

    return lambda x: function_from_prgr(x)


""""
        elif op == opcodes.SWAP:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            stack.append(tmp1)
            stack.append(tmp2)
        
"""
