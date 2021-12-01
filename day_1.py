from typing import List, Mapping


def ReadInput(filepath: str) -> List[str]:
    """Reads input from the text file"""
    input_strings = open(filepath, "r").readlines()
    return [line.strip() for line in input_strings]


def Main():
    input_as_list_str = ReadInput('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_1.txt')
    input_as_list_int = list(map(int, input_as_list_str))
    count = 0

    for index, num in enumerate(input_as_list_int):

        if index == 0:
            continue
        
        if input_as_list_int[index] - input_as_list_int[index-1] > 0:
            count += 1
    
    print('The number of times depth has increased is: {}'.format(count))


if __name__ == '__main__':
    Main()
