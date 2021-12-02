from typing import List

def ReadInput(filepath: str) -> List[str]:
    """Reads input from the text file as a list of strings"""
    input_strings = open(filepath, "r").readlines()
    return [line.strip() for line in input_strings]
