from typing import List

from utils.read_input import ReadInput


def CostFunctionPart1(input_state: List[int]):
    """Cost of moving in horizontal direction is 1 per step"""
    min_x = min(input_state)
    max_x = max(input_state)
    costs = []
    for i in range(min_x, max_x+1):
        cost = sum([abs(position - i) for position in input_state])
        costs.append(cost)
    
    min_index = costs.index(min(costs))
    print("Minimum Cost is at {} index: Cost is {}".format(min_index, costs[min_index]))


def APSum(num: int)-> int:
    return (num**2 + num)/2

def CostFunctionPart2(input_state: List[int]):
    """Cost for moving changes in Arithmetic progression manner"""
    min_x = min(input_state)
    max_x = max(input_state)
    costs = []
    for i in range(min_x, max_x+1):
        cost = sum([APSum(abs(position-i)) for position in input_state])
        costs.append(cost)
    
    min_index = costs.index(min(costs))
    print("Minimum Cost is at {} index: Cost is {}".format(min_index, costs[min_index]))


def Main():
    input_state = ReadInput('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_7.txt')[0].split(',')
    input_state = list(map(int, input_state))
    CostFunctionPart1(input_state)
    CostFunctionPart2(input_state)

if __name__ == '__main__':
    Main()