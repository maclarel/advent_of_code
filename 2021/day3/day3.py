# Part 1
zero_count = 0
ones_count = 0
gamma_rate = ""
epsilon_rate = ""

with open('input.txt') as f:
    data = f.read().split()
    for pos in range(len(data[0])):
        for i in data:
            if int(i[pos]) == 0:
                zero_count += 1
            else:
                ones_count += 1
        if zero_count > ones_count:
            gamma_rate += '0'
        else:
            gamma_rate += '1'
        zero_count = 0
        ones_count = 0

gamma_rate_int = int(gamma_rate, 2)

for i in range(len(gamma_rate)):
    if gamma_rate[i] == '0':
        epsilon_rate += '1'
    else:
        epsilon_rate += '0'

epsilon_rate_int = int(epsilon_rate, 2)

print(gamma_rate_int * epsilon_rate_int)

# Part 2
zero_count = 0

with open('input.txt') as f:
    orig_data = f.read().split() # get data as list of strings 
    
    data = orig_data
    for pos in range(len(data[0])):
        for i in data:
            if int(i[pos]) == 0:
                zero_count += 1
        if zero_count > len(data)/2:
            digit = '0'
        else:
            digit = '1'
        data = [i for i in data if i[pos] == digit]
        zero_count = 0
    oxy_gen_rating = data
    print(f'oxygen generator rating - {oxy_gen_rating}')
    
    data = orig_data
    for pos in range(len(data[0])):
        for i in data:
            if int(i[pos]) == 0:
                zero_count += 1
        if zero_count > len(data)/2:
            digit = '1'
        else:
            digit = '0'
        if len(data) != 1:
            data = [i for i in data if i[pos] == digit]
        zero_count = 0
    co2_scrub_rating = data
    print(f'co2 scrubber rating - {co2_scrub_rating}')

oxy_int = int(oxy_gen_rating[0], 2)
co2_int = int(co2_scrub_rating[0], 2)

print(f'part 2 - {oxy_int * co2_int}')
