# part 1 

d_pos = 0
h_pos = 0

with open('input.txt') as f:
    commands = f.read().splitlines()
    for c in commands: 
        c = list(c.split())
        val = int(c[1])
        if c[0] == "forward":
            h_pos += val
        elif c[0] == "down":
            d_pos += val
        else:
            d_pos -= val
        
        print(f'{c} hpos {h_pos} dpos {d_pos}')

print(d_pos*h_pos)

# part 2

d_pos = 0
h_pos = 0
aim = 0

with open('input.txt') as f:
    commands = f.read().splitlines()
    for c in commands: 
        c = list(c.split())
        val = int(c[1])
        if c[0] == "forward":
            h_pos += val
            d_pos += (val * aim)
        elif c[0] == "down":
            aim += val
        else:
            aim -= val
        print(f'{c} hpos {h_pos} dpos {d_pos} aim {aim}')

print(d_pos*h_pos)
