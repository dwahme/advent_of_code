import helpers
import functools

def get_compare_pages(rules):

    def compare_pages(left, right):
        return 1 if (right, left) in rules else -1

    return compare_pages

def task1(orders, pages_list):

    total = 0

    for pages in pages_list:
        
        sorted_pages = sorted(pages, key=functools.cmp_to_key(get_compare_pages(orders)))
        if pages == sorted_pages:
            middleIndex = int((len(pages) - 1)/2)
            
            total += int(pages[middleIndex])
    
    return total

def task2(orders, pages_list):

    total = 0

    for pages in pages_list:

        sorted_pages = sorted(pages, key=functools.cmp_to_key(get_compare_pages(orders)))
        if pages != sorted_pages:
            middleIndex = int((len(sorted_pages) - 1)/2)
            total += int(sorted_pages[middleIndex])
    
    return total

if __name__ == "__main__":
    lines = helpers.get_input("05")
    lines = [l.strip() for l in lines]

    split_index = lines.index("")
    orders = [(l.split("|")[0], l.split("|")[1]) for l in lines[:split_index]]
    pages_list = [pages.split(",") for pages in lines[split_index + 1:]]
    
    print(task1(orders, pages_list))
    print(task2(orders, pages_list))
