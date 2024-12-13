#8
def filter_evens(numbers: list[int]) -> list[int]:
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

list = [1,2,3,4,5,6,7,8]
print (filter_evens(list))

#9
def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reverse_words = []

    for i in range(len(words) -1,-1,-1):
        reverse_words.append(words[i])
    return ' '.join(reverse_words)

sentence = "123 456 789"
print(reverse_words(sentence))

#10
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    merged_dic = {}

    for key in dict1:
        merged_dic[key] = dict1[key]

    for key in dict2:
        merged_dic[key] = dict2[key]

    return merged_dic

dict1 = {"q": 100, "w": 200}
dict2 = {"c": 3, "v": 4}

print(merge_dicts(dict1, dict2))
