from statistics import mode

with open('input.txt') as f:
    data = f.read().strip()
    data = list(map(int, list(data.split(','))))

print(data)
target_loc = mode(data)
print(target_loc)
total_fuel_cost = 0
for f in data:
    total_fuel_cost += abs(f - target_loc)
print(total_fuel_cost)

#
# JANK
#

jank = []
for i in range(max(data)):
    total_fuel_cost = 0
    for f in data:
        total_fuel_cost += abs(f - i)
    jank.append(total_fuel_cost)

print(min(jank))

#
# JANK part 2
#

jank = []
for i in range(max(data)):
    total_fuel_cost = 0
    for f in data:
        movement = abs(f - i)
        for v in range(movement+1):
            total_fuel_cost += v
    jank.append(total_fuel_cost)

print(min(jank))
