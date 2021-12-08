with open('test2.txt') as f:
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

print(counter)

# part 2

data = [v[1] for v in [line.split(' | ') for line in start_data]] 

decode_dict = {
        'dgebacf': 8,
        'dcbef': 5,
        'cdgba': 2,
        'cefdb': 3,
        'bgf': 7,
        'cefbgd': 9,
        'gadfec': 6,
        'gecf': 4,
        'cagedb': 0,
        'gc': 1
        }

def cmp_strings(str1, str2):
    if all([i in str2 for i in str1]) and len(str1) == len(str2):
        return True

for i in data:
    num = ""
    split = i.split()
    for v in split:
        print(v)
        hits = 0
        for k in decode_dict.keys():
            if set(v) == set(k):
                print('key', k)
                hits += 1
                num += str(decode_dict[k])
                break

    print(num, hits)
    
