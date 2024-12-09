import helpers

def expand(compressed):

    out = []

    for i in range(0, len(compressed), 2):
        out += [ str(i // 2) ] * int(compressed[i])

        if i < len(compressed) - 1:
            out += [ "." ] * int(compressed[i + 1])
    
    return out


def checksum(disk_map):
    return sum([ int(val) * i for i, val in enumerate(disk_map) if val != "."])


def task1(lines):
    disk_map = expand(lines[0])

    prev_found = len(disk_map)

    for i in range(len(disk_map)):
        if disk_map[i] == ".":
            for j in range(prev_found - 1, i, -1):
                if disk_map[j] != disk_map[i]:
                    disk_map[i], disk_map[j] = disk_map[j], disk_map[i]
                    prev_found = j
                    break

    return checksum(disk_map)
    

def swap_region(disk_map, start1, start2, amount):
    for i in range(amount):
        disk_map[start1 + i], disk_map[start2 + i] = disk_map[start2 + i], disk_map[start1 + i]

def find_first_gap(disk_map, target_len, end):
    for idx, val in enumerate(disk_map):
        if idx + target_len > end:
            return None

        if val == ".":
            if all(disk_map[idx + i] == "." for i in range(target_len)):
                return idx
    return None

def task2(lines):

    disk_map = expand(lines[0])

    idx = len(disk_map)
    while idx > 0:
        if idx % 1000 == 0:
            print(f"{idx} / {len(disk_map)}")
        idx -= 1

        val = disk_map[idx]
        block_end = idx

        # we found a block, try to move it
        if val != ".":
            # get the full block
            while idx > 0 and disk_map[idx - 1] == val:
                idx -= 1

            # look for a gap to move the block to
            gap_len = block_end - idx + 1
            gap_start = find_first_gap(disk_map, gap_len, idx)

            if gap_start is not None:
                swap_region(disk_map, gap_start, idx, gap_len)

    return checksum(disk_map)

if __name__ == "__main__":
    lines = helpers.get_input("09")
    # lines = helpers.get_input("sample-09-01")
    # lines = helpers.get_input("sample-09-02")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
