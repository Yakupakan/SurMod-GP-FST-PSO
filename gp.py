import enum
import math
import random

opcodes = enum.Enum('opcodes', 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP NOP')

def eval(stack, program):
  while program != []:
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
      elif op == opcodes.SWAP:
        tmp1 = stack.pop()
        tmp2 = stack.pop()
        stack.append(tmp1)
        stack.append(tmp2)
      elif op == opcodes.NOP:
        pass
      else:
        stack.append(op)
  return stack
  
def random_program(n):
  prg = []
  func = list(opcodes)
  for i in range(0, n):
    if random.random() < 0.5:
      op = random.choice(func)
    else:
      op = random.randint(-2, 2)
    prg.append(op)
  return prg
  
def tournament_selection(fit, pop, t_size=4):
  tournament = random.choices(pop, k=t_size)
  return min(tournament, key=fit)
  
def two_points_crossover(x, y):
  k1 = random.randint(0, len(x)-1)
  k2 = random.randint(k1, len(x)-1)
  h1 = random.randint(0, len(y)-1)
  h2 = random.randint(h1, len(y)-1)
  of1 = x[0:k1] + y[h1:h2] + x[k2:]
  of2 = y[0:h1] + x[k1:k2] + y[h2:]
  return of1, of2
  
def mutation(x, p_m):
  def change(b):
    if random.random() < p_m:
      if random.random() < 0.5:
        op = random.choice(list(opcodes))
      else:
        op = random.randint(-2, 2)
      return op
    else:
      return b

  return [change(b) for b in x]
  
 def linear_GP(fit, pop_size, n_iter = 100):
  p_m = 0.1
  pop = [random_program(5) for _ in range(0, pop_size)]
  best = []
  for i in range(0, n_iter):
    selected = [tournament_selection(fit, pop) for _ in range(0, pop_size)]
    pairs = zip(selected, selected[1:] + [selected[0]])
    offsprings = []
    for x, y in pairs:
      of1, of2 = two_points_crossover(x, y)
      offsprings.append(of1)
      offsprings.append(of2)
    pop = [mutation(x, p_m) for x in offsprings]
    candidate_best = min(pop, key=fit)
    if fit(candidate_best) < fit(best):
      best = candidate_best
    if fit(best) == 0:
      return best
    # print(f"Best individual at generation {i}: {best}")
    print(f"Best fitness at generation {i}: {fit(best)}")
  return best
  
 def fit(prg):
  data = [(i, i**2 + 3*i + 2) for i in range(0, 100)]
  sq_errors = 0
  for x, y in data:
    try:
      stack = eval([x], prg)
    except Exception:
      return math.inf
    if stack == []:
      return math.inf
    else:
      sq_errors += (y - stack.pop())**2
  return sq_errors/len(data)
  
 random.seed(0)
linear_GP(fit, 100)
