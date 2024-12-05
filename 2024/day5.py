import helpers
import functools

def check_rule(pages, p, i, rule):
    left, right = rule

    if left not in pages or right not in pages:
        return True

    if left == p:
        return i < pages.index(right)
    if right == p:
        return pages.index(left) < i

    return True

def task1(orders, pages_list):

    total = 0

    for pages in pages_list:

        is_ok = True
        for i, p in enumerate(pages):
            for rule in orders:
                # found += helpers.call_and_print(check_rule, pages, p, i, rule)
                is_ok = is_ok and check_rule(pages, p, i, rule)

        if is_ok:
            # print(pages)
            middleIndex = int((len(pages) - 1)/2)
            # print(middleIndex)
            
            total += int(pages[middleIndex])
    
    return total

def get_compage_pages(rules, pages):

    rule_dict = { a: b for a, b in rules }
    
    def compare_pages(left, right):

        if (left, right) in rules:
            return -1
        if (right, left) in rules:
            return 1
        
        return -1

        # applicable_rules = [rule for rule in rules if right in rule_dict.keys() or right in rule_dict.values() ]
        # if not applicable_rules:
        #     print(f"{left} {right}: no applicable rule found")
        #     return -1

        all_ok = all(check_rule(pages, left, pages.index(left), rule) for rule in rules)
        print(f"{left} {right}: all_ok: {all_ok}")

        return -1 if all_ok else 1

    return compare_pages

def task2(orders, pages_list):

    total = 0

    for pages in pages_list:

        is_ok = True
        for i, p in enumerate(pages):
            for rule in orders:
                # is_ok = is_ok and check_rule(pages, p, i, rule)
                # print(pages, p, i, rule)
                is_ok = is_ok and check_rule(pages, p, i, rule)

        if not is_ok:
            print(pages)
            sorted_pages = sorted(pages, key=functools.cmp_to_key(get_compage_pages(orders, pages)))
            print(sorted_pages)
            middleIndex = int((len(sorted_pages) - 1)/2)
            # print(middleIndex)
            
            total += int(sorted_pages[middleIndex])
    
    return total

if __name__ == "__main__":
    lines = helpers.get_input("05")
    lines = [l.strip() for l in lines]

    split_index = lines.index("")
    orders = [(l.split("|")[0], l.split("|")[1]) for l in lines[:split_index]]
    pages_list = [pages.split(",") for pages in lines[split_index + 1:]]

    print(orders)
    print(pages_list)
    
    print(task1(orders, pages_list))
    print(task2(orders, pages_list))
