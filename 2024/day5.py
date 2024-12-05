import helpers
import functools

def get_compare_pages(rules):
    def compare_pages(left, right):
        return 1 if (right, left) in rules else -1

    return functools.cmp_to_key(compare_pages)

def pages_ok(pages, rules):
    return pages == sorted(pages, key=get_compare_pages(rules))

def get_middle(lst):
    return lst[int((len(lst) - 1)/2)]

def task1(orders, pages_list):
    return sum(get_middle(pages) for pages in pages_list if pages == sorted(pages, key=get_compare_pages(orders)))

def task2(orders, pages_list):
    return sum(get_middle(sorted(pages, key=get_compare_pages(orders))) for pages in pages_list if pages != sorted(pages, key=get_compare_pages(orders)))

if __name__ == "__main__":
    lines = helpers.get_input("05")
    lines = [l.strip() for l in lines]

    split_index = lines.index("")
    orders = [(int(l.split("|")[0]), int(l.split("|")[1])) for l in lines[:split_index]]
    pages_list = [[int(p) for p in pages.split(",")] for pages in lines[split_index + 1:]]
    
    print(task1(orders, pages_list))
    print(task2(orders, pages_list))
