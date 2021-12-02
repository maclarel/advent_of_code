with open('input.txt') as data:
    int_list = list(map(int, data.read().splitlines()))
    counter = 0
    sliding_counter = 0
   
    # non-sliding window
    for v in enumerate(int_list):
        current_val = int_list[v[0]]
        last_val = int_list[v[0]-1]
        if v[0] > 0 and current_val > last_val:
            counter += 1

    # sliding window
    for v in enumerate(int_list):
        current_val = sum([i for i in int_list[v[0]-3:v[0]]])
        last_val = sum([i for i in int_list[v[0]-4:v[0]-1]])
        if v[0] > 2 and current_val > last_val:
            sliding_counter += 1

    print(f"Total for non-sliding window: {counter}")
    print(f"Total for sliding window: {sliding_counter}")
