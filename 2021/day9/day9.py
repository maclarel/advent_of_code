with open('input.txt') as f:
    data=[[int(i) for i in l.strip()] for l in f]


row_count = len(data)
col_count = len(data[0])
risk_level = 0


[print(r) for r in data]
print(row_count, 'x', col_count)

# part 1

def check_surrounding(pos_row, pos_col):
    global risk_level
    # first row
    if pos_row == 0:
        if check_adjacent(pos_row, pos_col) and check_row_below(pos_row, pos_col):
            print(pos_row, pos_col, 'is', data[pos_row][pos_col])
            risk_level += data[pos_row][pos_col]+1
            print(f'risk level is now {risk_level}')
    # last row
    elif pos_row == row_count-1: 
        if check_adjacent(pos_row, pos_col) and check_row_above(pos_row, pos_col):
            print(pos_row, pos_col, 'is', data[pos_row][pos_col])
            risk_level += data[pos_row][pos_col]+1
            print(f'risk level is now {risk_level}')
    # other rows
    else:
        if check_adjacent(pos_row, pos_col) and check_row_above(pos_row, pos_col) and check_row_below(pos_row, pos_col):
            print(pos_row, pos_col, 'is', data[pos_row][pos_col])
            risk_level += data[pos_row][pos_col]+1
            print(f'risk level is now {risk_level}')

def check_adjacent(pos_row, pos_col):
    val = data[pos_row][pos_col]
    # col 1 to n-1
    if pos_col > 0 and pos_col < col_count-1: 
        if val < data[pos_row][pos_col-1] and val < data[pos_row][pos_col+1]:
            return True
    # col 0
    elif pos_col == 0:
        if val < data[pos_row][pos_col+1]:
            return True
    # col n
    else:
        if val < data[pos_row][pos_col-1]:
            return True

def check_row_above(pos_row, pos_col):
    val = data[pos_row][pos_col]
    # far left
    if pos_col == 0:
        if all([val < v for v in data[pos_row-1][pos_col:pos_col+1]]):
                return True
    # far right
    elif pos_col == col_count-1:
        if all([val < v for v in data[pos_row-1][pos_col-1:pos_col+1]]):
                return True
    # others
    else:
        if all([val < v for v in data[pos_row-1][pos_col-1:pos_col+1]]):
                return True

def check_row_below(pos_row, pos_col):
    val = data[pos_row][pos_col]
    # far left
    if pos_col == 0:
        if all([val < v for v in data[pos_row+1][pos_col:pos_col+1]]):
                return True
    # far right
    elif pos_col == col_count-1:
        if all([val < v for v in data[pos_row+1][pos_col-1:pos_col+1]]):
                return True
    # others
    else:
        if all([val < v for v in data[pos_row+1][pos_col-1:pos_col+1]]):
                return True
    
for row in range(row_count):
    for col in range(col_count):
        check_surrounding(row, col)

print(risk_level)
