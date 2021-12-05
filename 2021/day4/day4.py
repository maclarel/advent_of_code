with open('input.txt') as f:
    draw_order = list(map(int, list(f.readline().split(','))))
    f.readline() # being lazy and skipping the blank line
    data = f.read()

class Board:
    def __init__(self, data):
        self.rows = [] 
        for line in data.split('\n'):
            if line != '':
                self.rows.append(Row(line))
        self.cols = []
        for i in range(0,5):
            self.cols.append(Col([line.split()[i] for line in data.split('\n') if line != '']))

        self.matches = []
        self.nums = data

class Row(Board):
    def __init__(self, data):
        self.data = list(map(int, list(data.split())))
        self.hits = []
        #print('Created row with', self.data)

class Col(Board):
    def __init__(self, data):
        self.data = list(map(int, data))
        self.hits = []
        #print('Created col with', self.data)

split_data = [line for line in data.split('\n\n')]
boards = []

for board in split_data:
    boards.append(Board(board))

def check_winner():
    for i in draw_order:
        for board in boards:
            for row in board.rows:
                if i in row.data:
                    row.hits.append(i)
                    board.matches.append(i)
                    #print(row.data, row.hits)
                if len(row.hits) == 5:
                    print("WINNER! Found with final value:", i)
                    #print(row.data)
                    return board
            for col in board.cols:
                if i in col.data:
                    col.hits.append(i)
                    board.matches.append(i)
                if len(col.hits) == 5:
                    print("WINNER! Found with final value:", i)
                    #print(col.data)
                    return board


winning_board = check_winner()
print('Winning board:')
print(winning_board.nums)
print('Winning matches:')
marked_nums = set(winning_board.matches)
board_nums = list(map(int, list(winning_board.nums.split())))
print(marked_nums)
print(board_nums)
print('Sum of unmarked:', sum([i for i in board_nums if i not in marked_nums]))

#part 2

winning_boards = []
def check_loser():
    for i in draw_order:
        for board in boards:
            for row in board.rows:
                if i in row.data:
                    row.hits.append(i)
                    board.matches.append(i)
                if len(row.hits) == 5:
                    print("WINNER! Found with final value:", i)
                    winning_boards.append(board)
                    if board in boards:
                        boards.remove(board)
            for col in board.cols:
                if i in col.data:
                    col.hits.append(i)
                    board.matches.append(i)
                if len(col.hits) == 5:
                    print("WINNER! Found with final value:", i)
                    winning_boards.append(board)
                    if board in boards:
                        boards.remove(board)
                    
check_loser()
print('Losing board:')
losing_nums = winning_boards[-1].nums
print(losing_nums)
print('Losing board matches:')
losing_marked_nums = set(winning_boards[-1].matches)
losing_board_nums = list(map(int, losing_nums.split()))
print(losing_marked_nums)
print('Sum of unmarked:', sum([i for i in losing_board_nums if i not in losing_marked_nums]))
