from typing import List

from utils.read_input import ReadInput


def Simulate(state: List, days: int) -> List:
    lanternfish_dict = {i: 0 for i in range(0,9)}

    for day_to_egg in state:
        lanternfish_dict[day_to_egg] += 1

    for day in range(1, days+1):
        temp = lanternfish_dict[0]
        lanternfish_dict[0] = lanternfish_dict[1]
        lanternfish_dict[1] = lanternfish_dict[2]
        lanternfish_dict[2] = lanternfish_dict[3]
        lanternfish_dict[3] = lanternfish_dict[4]
        lanternfish_dict[4] = lanternfish_dict[5]
        lanternfish_dict[5] = lanternfish_dict[6]
        lanternfish_dict[6] = temp + lanternfish_dict[7]
        lanternfish_dict[7] = lanternfish_dict[8]
        lanternfish_dict[8] = temp
    
    return sum(lanternfish_dict.values())


def Main():
    input_state = ReadInput('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_6.txt')[0].split(',')
    input_state = list(map(int, input_state))
    print('Number of lanternfish: {}'.format(Simulate(input_state, days=256)))

if __name__ == '__main__':
    Main()
