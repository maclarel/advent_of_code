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
