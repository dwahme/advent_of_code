import helpers

def expand(compressed):

    out = []

    for i in range(0, len(compressed), 2):
        out += [ str(i // 2) ] * int(compressed[i])

        if i < len(compressed) - 1:
            out += [ "." ] * int(compressed[i + 1])
    
    return out

def expand2(compressed):

    out = []
    
    for i in range(0, len(compressed), 2):
        out += [(int(compressed[i]), str(i // 2))]

        if i < len(compressed) - 1:
            out += [(int(compressed[i + 1]), ".")]
    
    return out

def convert_expand2(disk_map):
    out = []
    for amount, val in disk_map:
        out += [str(val)] * amount

    return out


def checksum(disk_map):
    return sum([ int(val) * i for i, val in enumerate(disk_map) if val != "."])


def task1(lines):
    disk_map = expand(lines[0])

    # backwards = disk_map[::-1]

    len_map = len(disk_map)
    prev_found = len(disk_map)

    for i in range(len(disk_map)):
        # if i % 1000 == 0:
        #     print(f"{i} / {len_map}")
        if disk_map[i] == ".":
            for j in range(prev_found - 1, i, -1):
                if disk_map[j] != disk_map[i]:
                    disk_map[i], disk_map[j] = disk_map[j], disk_map[i]
                    prev_found = j
                    # print(i, j)
                    break

    return checksum(disk_map)
    

def swap_region(disk_map, start1, start2, amount):
    for i in range(amount):
        disk_map[start1 + i], disk_map[start2 + i] = disk_map[start2 + i], disk_map[start1 + i]

def find_first_gap(disk_map, target_len, end):
    for idx, val in enumerate(disk_map):
        if idx + target_len > end:
            break

        if val == ".":
            if all(disk_map[idx + i] == "." for i in range(target_len)):
                return idx
    return None

def task2(lines):

    disk_map = expand(lines[0])
    # print("".join(disk_map))

    i = len(disk_map)
    while i > 0:
        if i % 1000 == 0:
            print(f"{i} / {len(disk_map)}")
        i -= 1

        val, end = disk_map[i], i

        # we found a block, try to move it
        if val != ".":

            # get the full block
            while i > 0 and disk_map[i - 1] == val:
                # start -= 1
                i -= 1

            # look for a gap to move the block to
            gap_len = end - i + 1
            gap_start = find_first_gap(disk_map, gap_len, i)

            if gap_start is not None:
                swap_region(disk_map, gap_start, i, gap_len)
                # print("".join(disk_map))
    # print("".join(disk_map))

    return checksum(disk_map)

if __name__ == "__main__":
    lines = helpers.get_input("09")
    # lines = helpers.get_input("sample-09-01")
    # lines = helpers.get_input("sample-09-02")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
