import enum

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
            stack.append(op1 / op2)
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
        else:
            stack.append(op)
    return stack


""""
        elif op == opcodes.SWAP:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            stack.append(tmp1)
            stack.append(tmp2)
        
"""
