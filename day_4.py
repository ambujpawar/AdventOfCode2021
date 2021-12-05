from typing import List, Tuple

from utils.read_input import ReadInput

class LotteryTicket():
    def __init__(self, numbers: List[List[int]]):
        assert len(numbers) == 5

        flat_number_list = [[int(num), False] for row in numbers for num in row.split()]
        self.numbers = flat_number_list
        self.row_size = 5
        self.column_size = 5

        assert len(self.numbers) == 25


    def TickOneNumber(self, called_number: int):
        for number in self.numbers:
            if number[0] == called_number:
                number[1] = True
    

    def IsRowComplete(self) -> bool:
        for i in range(0, 25, 5):
            row = self.numbers[i: i+5]
            if all(num[1] for num in row) == True:
                return True
        return False

    def IsColumnComplete(self) -> bool:
        for i in range(0, 5):
            column = [self.numbers[i], self.numbers[i+5], self.numbers[i+10], self.numbers[i+15], self.numbers[i+20]]
            if all(num[1] for num in column) == True:
                return True
        return False
    
    def IsBingo(self) -> bool:
        if self.IsRowComplete() or self.IsColumnComplete():
            return True
        return False


def ReadLotteryInput(filepath: str):
    """Reads the lottery input and return the tuple of lottery input and lottery ticket"""
    lottery_input = ReadInput(filepath)
    called_numbers = list(map(int, lottery_input[0].split(",")))
    tickets = []
    for index in range(2, len(lottery_input) -1, 6):
        ticket = lottery_input[index: index + 5]
        tickets.append(LotteryTicket(ticket))
    
    return called_numbers, tickets


def GetMagicTicket(called_numbers: List[int], tickets: LotteryTicket):
    for called_num in called_numbers:
        for ticket in tickets:
            ticket.TickOneNumber(called_num)
            if ticket.IsBingo():
                return called_num, ticket


def SolutionPart1(called_num: int, magic_ticket: LotteryTicket):
    sum_num = 0
    for num in magic_ticket.numbers:
        if num[1] == False:
            sum_num += num[0]
    return sum_num*called_num


def TicketToWinLast(called_numbers: List[int], tickets: List[LotteryTicket]):
    winner_tickets = []
    total_tickets = len(tickets)

    for called_num in called_numbers:
        for ticket in tickets:

            if ticket not in winner_tickets:
                ticket.TickOneNumber(called_num)

                if total_tickets - len(winner_tickets) == 1:
                    # This is the last ticket to be completed and the number which makes it bingo
                    if ticket.IsBingo():
                        return called_num, ticket

                else:
                    if ticket.IsBingo():
                        winner_tickets.append(ticket)
                    

def Main():
    called_numbers, tickets = ReadLotteryInput('/Users/ambuj/Desktop/GithubProjects/AdventOfCode2021/data/day_4.txt')

    called_num, magic_ticket =  GetMagicTicket(called_numbers, tickets)
    print("The solution to Part1 is: {}".format(SolutionPart1(called_num, magic_ticket)))

    called_num, last_ticket = TicketToWinLast(called_numbers, tickets)
    print("The solution to Part2 is: {}".format(SolutionPart1(called_num, last_ticket)))


if __name__ == '__main__':
    Main()
