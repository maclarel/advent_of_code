fish = {}.fromkeys(['0','1','2','3','4','5','6','7','8','holding8', 'holding6'], 0)
current_day = 1

with open('input.txt') as f:
    data = f.read().strip('\n').split(',')

for i in data:
    fish[i] += 1 

while current_day <= 256:
    for i in range(0,9): 
        if i == 0:
            fish['holding8'] = fish['0']
            fish['holding6'] = fish['0']
        else:
            j = str(i-1)
            fish[str(j)] = fish[str(i)]
    fish['6'] += fish['holding6']
    fish['8'] = fish['holding8']
    current_day += 1

total_fish = 0
for i in range(0,9):
    total_fish += fish[str(i)]
print(total_fish)
