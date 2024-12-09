import helpers

def expand(compressed):

    out = []

    for i in range(0, len(compressed), 2):
        out += [ i // 2 ] * int(compressed[i])

        if i < len(compressed) - 1:
            out += [ None ] * int(compressed[i + 1])
    
    return out

def checksum(disk_map):
    return sum([ val * i for i, val in enumerate(disk_map) if val is not None])

def task1(lines):
    disk_map = expand(lines[0])

    prev_found = len(disk_map)

    for i in range(len(disk_map)):
        if disk_map[i] is None:
            for j in range(prev_found - 1, i, -1):
                if disk_map[j] is not None:
                    disk_map[i] = disk_map[j]
                    disk_map[j] = None
                    prev_found = j
                    break

    return checksum(disk_map)

def task2(lines):
    
    # (block value, num spaces)
    data = [ (idx // 2 if idx % 2 == 0 else None, int(val)) for idx, val in enumerate(lines[0]) ]
    
    for i in range(len(data) - 1, -1, -1):
        block_value, block_spaces = data[i]

        if block_value is not None:
            for j in range(i):
                target_value, target_spaces = data[j]

                if target_value is None and target_spaces >= block_spaces:
                    # swap the data
                    data[j] = (block_value, block_spaces)
                    data[i] = (None, block_spaces)

                    # we had leftover space, make sure it doesn't disappear
                    if target_spaces > block_spaces:
                        data.insert(j + 1, (None, target_spaces - block_spaces))
                    break

    expanded = [[val] * num for val, num in data]
    flattened = [x for xs in expanded for x in xs]
    return checksum(flattened)

if __name__ == "__main__":
    lines = helpers.get_input("09")
    # lines = helpers.get_input("sample-09-01")
    # lines = helpers.get_input("sample-09-02")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
