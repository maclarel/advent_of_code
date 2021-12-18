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

total_score = 0

def parse_line(line):
    last_opening_char = []
    print("parsing line", line)
    for c in line:
        print('evaling', c)
        if c in chars.keys():
            last_opening_char.append(c)
            print('looks like opening char, adding to last_opening_char')
        elif c in chars.values():
            if c != chars[last_opening_char[-1]]:
                print(f"Expected {chars[last_opening_char[-1]]}, but found {c} instead.")
                return points_lookup[c]
                break
            print("found match, removing", last_opening_char.pop())
    return 0

    print("completed parsing")


for line in data:
    total_score += parse_line(line)

# part 1
print(total_score)
