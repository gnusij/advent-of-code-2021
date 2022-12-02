import numpy as np
import aocvar
from aocvar.core import Puzzle 

def count_increase(intList):
    increase_count = 0
    for i in range(1, len(intList)):
        if int(intList[i]) > int(intList[i-1]):
            increase_count += 1
    return increase_count

def intlist(input_str:str) -> list:
    return [int(inp) for inp in input_str.splitlines()]

def sum_window(intList:list, size:int) -> list:
    sum_windowed_list = []
    for i in range(len(intList)-size-1):
        sum_windowed_list.append( sum([int(intList[i+j]) for j in range(size)]) )
    return sum_windowed_list

p = aocvar.puzzle(year=2021,day=1)
p.input = 'input.txt'
p.solver_a = lambda x: count_increase(intlist(x))
p.solver_b = lambda x: count_increase(sum_window(intlist(x),3))