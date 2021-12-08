with open('input.txt') as f:
    start_data = [ line.strip() for line in f.readlines()]

# part 1

data = [v[1] for v in [line.split(' | ') for line in start_data]]
counter = 0
len_dict = {
        'one': 2,
        'four': 4,
        'seven': 3,
        'eight': 7
}

for i in data:
    split = i.split()
    for v in split:
        if len(v) in len_dict.values():
            counter += 1

print('p1', counter)

# part 2

from collections import defaultdict

d1 = [v[0] for v in [line.split(' | ') for line in start_data]] 
d2 = [v[1] for v in [line.split(' | ') for line in start_data]] 
len_dict = {
        '1': 2,
        '4': 4,
        '7': 3,
        '8': 7
}
total_val = 0
for line in start_data:
    decode_dict = defaultdict(None)
    data = line.split(' | ')
    row_val = ""
    # identify our unique-length vals
    for val in data[0].split():
        if len(val) in len_dict.values():
            key = [k for k, v in len_dict.items() if v == len(val)]
            decode_dict[key[0]] = val
    # identify 2, 3, and 5
    for val in data[0].split():
        if len(val) == 5:
            if len([l for l in set(val) if l in set(decode_dict['1'])]) == len(decode_dict['1']):
                decode_dict['3'] = val
            elif len([v for v in set(decode_dict['1']) | set(decode_dict['4']) if v in set(val)]) == 2:
                decode_dict['2'] = val
            else:
                decode_dict['5'] = val
    # identify 0, 6, 9
    for val in data[0].split():
        if len(val) == 6:
            if len(set(val).difference(set(decode_dict['5']))) == 2:
                decode_dict['0'] = val
            elif len(set(val).difference(set(decode_dict['1']))) == 4:
                decode_dict['9'] = val
            else:
                decode_dict['6'] = val

    for val in data[1].split():
        row_val += [k for k,v in decode_dict.items() if set(v) == set(val)][0]

    #print(row_val)
    total_val += int(row_val)

print(total_val)

