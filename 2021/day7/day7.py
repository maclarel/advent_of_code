with open('input.txt') as f:
    data = f.read().strip()
    data = list(map(int, list(data.split(','))))

# part 1

crab_blaster_locs = {}
for i in range(max(data)):
    total_fuel_cost = 0
    for f in data:
        total_fuel_cost += abs(f - i)
    crab_blaster_locs[i]=total_fuel_cost

min_cost = min(crab_blaster_locs.values())
print('min cost', min_cost)

for loc, val in crab_blaster_locs.items():
    if val == min_cost:
        print('target loc =', loc)

# JANK part 2

crab_blaster_locs = {}
for i in range(max(data)):
    total_fuel_cost = 0
    for f in data:
        movement = abs(f - i)
        total_fuel_cost += movement*(movement+1)/2 # https://www.cuemath.com/sum-of-natural-numbers-formula/
    crab_blaster_locs[i] = total_fuel_cost

min_cost = int(min(crab_blaster_locs.values()))
print('min cost', min_cost)

for loc, val in crab_blaster_locs.items():
    if val == min_cost:
        print('target loc =', loc)
