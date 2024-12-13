#11
def sort_words(words: list[str]) -> list[str]:
    sorted_words = sorted(words)
    return sorted_words

list_word = ["tree","leaf","flower"]
print(sort_words(list_word))

#12
def common_items(list1: list, list2: list) -> list:
    common = []

    for item in list1:
        if item in list2:
            common.append(item)
    return common

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
print(common_items(list1,list2))

#13
def multiplication_table(n: int) -> list[str]:
    table = []
        for i in range(1,11):
