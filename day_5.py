from typing import List, Tuple

from utils.read_input import ReadInput


class AirVents:

    def __init__(self, grid_size) -> None:
        self.rows = grid_size[0]
        self.columns = grid_size[1]
        self.position = []
        
        for row in range(self.rows):
            self.position.append([0] * self.columns)
    
     
    def OpenVent(self, initial_position, final_position):
        # assert initial_position[0] == final_position[0] or initial_position[1] == final_position[1]
        
        # Open only the vents in the same row
        if initial_position[0] == final_position[0]:
            min_pos, max_pos = min(initial_position[1], final_position[1]), max(initial_position[1], final_position[1])
            # Plus 1 because you to include the max_pos as well
            for index in range(min_pos, max_pos+1):
                self.position[index][initial_position[0]] += 1
        
        # Open the vents in the same column
        elif initial_position[1] == final_position[1]:
            min_pos, max_pos = min(initial_position[0], final_position[0]), max(initial_position[0], final_position[0])
            # Plus 1 because you to include the max_pos as well
            for index in range(min_pos, max_pos+1):
                self.position[initial_position[1]][index] += 1

        else:
            # Diagonal lines
            # Step 1- Mark initial point
            points_to_mark = abs(initial_position[0] - final_position[0])

            # Special case
            if initial_position[0] > final_position[0]:
                initial_position, final_position = final_position, initial_position
            
            if initial_position[0] < final_position[0]:
                for i in range(points_to_mark+1):

                    if initial_position[1] < final_position[1]:

                        if initial_position[0] + i == final_position[0] and initial_position[1] + i == final_position[1]:
                            self.position[final_position[1]][final_position[0]] += 1
                        else:
                            self.position[initial_position[1] + i][initial_position[0] + i] += 1

                    else:
                        if initial_position[0] + i == final_position[0] and initial_position[1] - i == final_position[1]:
                            self.position[final_position[1]][final_position[0]] += 1
                        else:
                            self.position[initial_position[1] - i][initial_position[0] + i] += 1


    def CountOverlap(self) -> int:
        overlap = 0 
        for row in self.position:
            for num in row:
                if num >= 2:
                    overlap += 1
        return overlap


def Main():
    commands = ReadInput('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_5.txt')
    grid = AirVents(grid_size=(1000, 1000))
    print(grid)

    for command in commands:
        initial_parse_pos, final_parse_pos = command.split('->')
        initial_pos = tuple(map (int, initial_parse_pos.split(',')))
        final_pos = tuple(map (int, final_parse_pos.split(',')))
        grid.OpenVent(initial_pos, final_pos)
    
    print('Number of overlap: {}'.format(grid.CountOverlap()))


if __name__ == '__main__':
    Main()