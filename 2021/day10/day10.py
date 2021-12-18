with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

chars = {
        "[": "]",
        "(": ")",
        "{": "}",
        "<": ">"
        }

points_lookup = {
        "]": 57,
        ")": 3,
        "}": 1197,
        ">": 25137
        }

points_lookup2 = {
        "]": 2,
        ")": 1,
        "}": 3,
        ">": 4
        }

def parse_line(line):
    last_opening_char = []
    for c in line:
        if c in chars.keys():
            last_opening_char.append(c)
        elif c in chars.values():
            if c != chars[last_opening_char[-1]]:
                return points_lookup[c]
                break
            last_opening_char.pop()
    return 0

def complete_line(line):
    score = 0
    last_opening_char = []
    for c in line:
        if c in chars.keys():
            last_opening_char.append(c)
        elif c in chars.values():
            last_opening_char.pop()
    for val in last_opening_char[::-1]:
        closing_char = chars[last_opening_char.pop()]
        score = score * 5 + points_lookup2[closing_char]
    return score

# part 1
total_score = 0

for line in data:
    total_score += parse_line(line)

print("part 1:", total_score)

# part 2
scores = []
for line in data:
    if parse_line(line) == 0:
        scores.append(complete_line(line))
scores.sort()
midpoint = int(len(scores)/2)
print("part 2:", scores[midpoint])
