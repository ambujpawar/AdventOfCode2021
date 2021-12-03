from collections import Counter
from typing import List, Tuple
from statistics import mode

from utils.read_input import ReadInput


def ReadInputColumnWise(filepath: str) -> Tuple[List[str], List[str]]:
    """Reads a file and outputs the result columnwise"""
    input_strings = ReadInput(filepath)
    rows = [[x for x in row] for row in input_strings]
    cols = [list(col) for col in zip(*rows)]
    return input_strings, cols


def InvertBinaryString(binary_string: str) -> str:
    """Inverts a binary string"""
    epsilon = ''
    for char in binary_string:
        if char == '1':
            epsilon += '0'
        elif char == '0':
            epsilon += '1'
        else:
            raise Exception('Expected only 1 and 0 got {}'.format(char))
    return epsilon


def ConvertRowwiseToColumns(rows: List[str]):
    rows = [[x for x in row] for row in rows]
    cols = [list(col) for col in zip(*rows)]
    return cols

def FindOxygenRating(valid_strings: List[str]):
    max_len = len(valid_strings[0])
    for index in range(max_len):
        col = ConvertRowwiseToColumns(valid_strings)[index]
        counts = Counter(col)
        if counts['1'] >= counts['0']:
            most_frequent = '1'
        else:
            most_frequent = '0'

        valid_strings = [input_str for input_str in valid_strings if input_str[index] == most_frequent] 

        if len(valid_strings) == 1:
            return valid_strings[0]

    return None


def FindCO2Rating(valid_strings: List[str]):
    max_len = len(valid_strings[0])
    for index in range(max_len):
        col = ConvertRowwiseToColumns(valid_strings)[index]
        counts = Counter(col)
        if counts['1'] < counts['0']:
            least_frequent = '1'
        else:
            least_frequent = '0'

        valid_strings = [input_str for input_str in valid_strings if input_str[index] == least_frequent] 

        if len(valid_strings) == 1:
            return valid_strings[0]

    return None


def Main():
    input_strings, cols = ReadInputColumnWise('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_3.txt')
    gamma = ''.join([mode(col) for col in cols])
    epsilon = InvertBinaryString(gamma)
    gamma_as_int = int(gamma, 2)
    epsilon_as_int = int(epsilon, 2)
    print('The answer to the first part is {}'.format(gamma_as_int*epsilon_as_int))

    # Part 2
    oxygen = FindOxygenRating(input_strings)
    co2 = FindCO2Rating(input_strings)
    oxygen_as_int = int(oxygen, 2)
    co2_as_int =int(co2, 2)
    print('Solution for part 2 is: {}'.format(oxygen_as_int*co2_as_int))

if __name__ == '__main__':
    Main()


