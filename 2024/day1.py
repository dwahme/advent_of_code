
def get_distance(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)

    total = 0
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    
    return total

def get_similarity(l1, l2):

    total = 0
    for i in l1:
        num_appearances = len([j for j in l2 if j == i])
        total += i * num_appearances
    
    return total

if __name__ == "__main__":
    with open("inputs\\day1.txt", "r") as f:
        lines = f.readlines()
    
    lst1 = [int(l.split()[0].strip()) for l in lines]
    lst2 = [int(l.split()[1].strip()) for l in lines]

    print(get_distance(lst1, lst2))

    print(get_similarity(lst1, lst2))
