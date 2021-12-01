import numpy as np
from typing import List, Mapping


def ReadInput(filepath: str) -> List[str]:
    """Reads input from the text file"""
    input_strings = open(filepath, "r").readlines()
    return [line.strip() for line in input_strings]


def NumDepthIncreased(input_as_list_int: List[int]) -> int:
    """Returns the number of times the depth has increased"""
    count = 0
    for index, _ in enumerate(input_as_list_int):
        if index == 0:
            continue
        if input_as_list_int[index] - input_as_list_int[index-1] > 0:
            count += 1
    return count


def SlidingWindowSum(input_as_list_int: List[int], window_size: int =3) -> List[int]:
    """Returns the sliding window sum for a provided window size"""
    numpy_array = np.array(input_as_list_int)
    sliding_window_sum = np.convolve(numpy_array, np.ones(window_size, dtype=int), mode='valid')
    return sliding_window_sum


def Main():
    input_as_list_str = ReadInput('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_1.txt')
    input_as_list_int = list(map(int, input_as_list_str))
    
    count = NumDepthIncreased(input_as_list_int)
    count_2 = NumDepthIncreased(SlidingWindowSum(input_as_list_int))

    print('The Solution for Part 1 is: {}'.format(count))
    print('The Solution for Part 2 is: {}'.format(count_2))


if __name__ == '__main__':
    Main()
