with open('input.txt') as f:
    data = f.read().split('\n')
    split_data = [pair.split(' -> ') for pair in data]
    
dict_data = {}
for val in enumerate(split_data):
    if len(val[1]) > 1:
        #print(val[1][0].split(',')[0])
        #print(val[1][1].split(',')[0])
        dict_data[val[0]] = dict(x1 = int(val[1][0].split(',')[0]), y1 = int(val[1][0].split(',')[1]), x2 = int(val[1][1].split(',')[0]), y2 = int(val[1][1].split(',')[1]))

# Get max board size
max_x = max(max({v['x1'] for k,v in dict_data.items()}),max({v['x2'] for k,v in dict_data.items()}))
max_y = max(max({v['y1'] for k,v in dict_data.items()}),max({v['y2'] for k,v in dict_data.items()}))

table = []
for i in range(max_y+1):
    table.append([0 for v in range(max_x+1)])

print('starting board')
# [print(row) for row in table] # don't need to show with real data

for v in dict_data.items():
    if v[1]['x1'] == v[1]['x2']: #print('y range', v[1]['y1'], v[1]['y2'])
        min_y_val = min(v[1]['y1'], v[1]['y2'])
        max_y_val = max(v[1]['y1'], v[1]['y2'])
        for i in range(min_y_val, max_y_val+1):
            table[i][v[1]['x1']] += 1

    if v[1]['y1'] == v[1]['y2']:
        #print('x range', v[1]['x1'], v[1]['x2'])
        min_x_val = min(v[1]['x1'], v[1]['x2'])
        max_x_val = max(v[1]['x1'], v[1]['x2'])
        for i in range(min_x_val, max_x_val+1):
            table[v[1]['y1']][i] += 1

print('completed board for part 1')
#[print(row) for row in table] # don't need to show with real data

overlap = 0
for row in table:
    for i in row:
        if i > 1:
            overlap += 1
print('num overlapping locations in part 1', overlap)

# part 2

print('updating board for part 2')

for v in dict_data.items():
    if abs(v[1]['x1'] - v[1]['x2']) == abs(v[1]['y1'] - v[1]['y2']):
        min_y_val = min(v[1]['y1'], v[1]['y2'])
        max_y_val = max(v[1]['y1'], v[1]['y2'])
        min_x_val = min(v[1]['x1'], v[1]['x2'])
        max_x_val = max(v[1]['x1'], v[1]['x2'])

        x_range = list(range(min_x_val, max_x_val+1))
        if v[1]['x1'] > v[1]['x2']:
            x_range.reverse()
        #print(x_range)
            
        y_range = list(range(min_y_val, max_y_val+1))
        if v[1]['y1'] > v[1]['y2']:
            y_range.reverse()
        #print(y_range)
        
        zipped = zip(x_range, y_range)
        for i in set(zipped):
            table[i[1]][i[0]] += 1
        #[print(row) for row in table] # don't need to show with real data
                  
print('completed board for part 2')
#[print(row) for row in table] # don't need to show with real data

overlap = 0
for row in table:
    for i in row:
        if i > 1:
            overlap += 1
print('num overlapping locations in part 2', overlap)
