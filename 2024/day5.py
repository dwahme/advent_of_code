import helpers
import functools

def get_middle(lst):
    return lst[int((len(lst) - 1)/2)]

def task1(compare_pages, pages_list):
    return sum(get_middle(pages) for pages in pages_list if pages == sorted(pages, key=compare_pages))

def task2(compare_pages, pages_list):
    return sum(get_middle(sorted(pages, key=compare_pages)) for pages in pages_list if pages != sorted(pages, key=compare_pages))

if __name__ == "__main__":
    lines = helpers.get_input("05")
    lines = [l.strip() for l in lines]

    split_index = lines.index("")
    orders = [(int(l.split("|")[0]), int(l.split("|")[1])) for l in lines[:split_index]]
    pages_list = [[int(p) for p in pages.split(",")] for pages in lines[split_index + 1:]]

    compare_pages = functools.cmp_to_key(lambda left, right: 1 if (right, left) in orders else -1)
    
    print(task1(compare_pages, pages_list))
    print(task2(compare_pages, pages_list))
