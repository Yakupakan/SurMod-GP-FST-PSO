"""
extending eval.py script adding other function to the function dataset
"""
import enum
import math
import numpy as np

opcodes = enum.Enum('opcodes', 'PLUS MINUS TIMES DIVIDE MOD DUP NOP')


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
                pass
        elif op == opcodes.MOD:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 % op2)
        elif op == opcodes.DUP:
            tmp = stack.pop()
            stack.append(tmp)
            stack.append(tmp)
        elif op == opcodes.NOP:
            pass
        elif op == opcodes.SIN:
            if isinstance(stack[-1], float):
                tmp = stack.pop()
                stack.append(np.sin(tmp))
        elif op == opcodes.COS:
            if isinstance(stack[-1], float):
                tmp = stack.pop()
                stack.append(np.cos(tmp))
        elif op == opcodes.EXP:
            tmp = stack.pop()
            stack.append(np.exp(tmp))
        else:
            stack.append(op)
    return stack


def make_function(program):
    """
    Function that takes a program as input and returns a function that perform the described program
    :param program: program considered
    :return: function that emulates the program
    """

    def function_from_prgr(x, program=program):
        stack = x
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
                    pass
            elif op == opcodes.MOD:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 % op2)
            elif op == opcodes.DUP:
                tmp = stack.pop()
                stack.append(tmp)
                stack.append(tmp)
            elif op == opcodes.NOP:
                pass
            elif op == opcodes.SIN:
                if isinstance(stack[-1], float):
                    tmp = stack.pop()
                    stack.append(np.sin(tmp))
            elif op == opcodes.COS:
                if isinstance(stack[-1], float):
                    tmp = stack.pop()
                    stack.append(np.cos(tmp))
            elif op == opcodes.EXP:
                tmp = stack.pop()
                stack.append(np.exp(tmp))
            else:
                stack.append(op)
        return stack[-1]  # in the last value of the stack is collected the value of the fitness

    return lambda x: function_from_prgr(x)


""""
        elif op == opcodes.SWAP:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            stack.append(tmp1)
            stack.append(tmp2)
        
"""
