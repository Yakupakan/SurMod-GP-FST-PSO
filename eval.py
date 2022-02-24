import enum
import math
from hyperparam import enum_set

opcodes = enum.Enum('opcodes', enum_set)  # MOD = DUP


def make_function(program):
    """
    Function that takes a program as input and returns a function that perform the described program
    :param program: program considered
    :return: function that emulates the program
    """

    def function_from_prgr(x, program=program):
        # stack = [0, 0] + x  # adding [0, 0] to make compilable all the programs as [opcodes.MINUS]
        stack = x.copy()  # adding [0, 0] to make compilable all the programs as [opcodes.MINUS]

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
                if op2 == 0:
                    return 10 ** 6
                else:
                    stack.append(op1 / op2)
            elif op == opcodes.MOD:
                op1 = stack.pop()
                op2 = stack.pop()
                if op2 == 0:
                    return 10 ** 6
                else:
                    stack.append(op1 % op2)
            elif op == opcodes.DUP:
                tmp = stack.pop()
                stack.append(tmp)
                stack.append(tmp)
            elif op == opcodes.SWAP:
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp1)
                stack.append(tmp2)
            elif op == opcodes.NOP:
                pass
            else:
                stack.append(op)
        if stack:
            return stack.pop()  # in the last value of the stack is collected the value of the fitness
        else:
            return 10*+6

    return lambda x: function_from_prgr(x)


""""

def eval(input_stack, program):
    stack = input_stack.copy()
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
            if op2 == 0:
                return 10 ** 6
            else:
                stack.append(op1 / op2)
        else:
            stack.append(op)
    return stack.pop()

elif op == opcodes.SWAP:
    tmp1 = stack.pop()
    tmp2 = stack.pop()
    stack.append(tmp1)
    stack.append(tmp2)
elif op == opcodes.DUP:
    tmp = stack.pop()
    stack.append(tmp)
    stack.append(tmp)  
"""
