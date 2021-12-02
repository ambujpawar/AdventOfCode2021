from typing import List, Tuple

from utils.read_input import ReadInput

POSSIBLE_DIRECTIONS = ['forward', 'up', 'down']

def FindFinalPosition(instructions: List[str]):
    """Given a list of directions it predicts what the final position of the submarine is"""
    x = 0
    y = 0

    for instruction in instructions:
        direction, step = instruction.split()[0].lower(), int(instruction.split()[-1])
        
        if 'forward' in direction:
            x += step
        
        elif 'up' in direction:
            y -= step
        
        elif 'down' in direction:
            y += step
        
        else:
            return Exception('Unknown direction found. Only possible directions are {}'.format(POSSIBLE_DIRECTIONS))
    
    return x,y

def FinFinalPositionWithAim(instructions: List[str]):
    """Find final position based on the aim as described in the manual"""
    x = 0
    y = 0
    aim = 0

    for instruction in instructions:
        direction, step = instruction.split()[0].lower(), int(instruction.split()[-1])
        
        if 'forward' in direction:
            x += step
            y += aim*step

        
        elif 'up' in direction:
            aim -= step
        
        elif 'down' in direction:
            aim += step
        
        else:
            return Exception('Unknown direction found. Only possible directions are {}'.format(POSSIBLE_DIRECTIONS))
    
    return x,y


def Main():
    instructions = ReadInput('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_2.txt')
    final_position = FindFinalPosition(instructions)
    print(f'The final position is {final_position}')
    print(f'The answer to first part is {final_position[0] * final_position[1]}')

    final_position_with_aim = FinFinalPositionWithAim(instructions)
    print(f'The final position is {final_position_with_aim}')
    print(f'The answer to second part is {final_position_with_aim[0] * final_position_with_aim[1]}')

if __name__ == '__main__':
    Main()