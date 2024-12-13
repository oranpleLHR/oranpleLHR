#4
def count_vowels(text: str) -> int:
    vowels = "aeiou"
    return sum(1 for char in text if char in vowels)

text = input("enter the text: ")
vowel = count_vowels(text)

print(f"the number of vowels is: {vowel}")

#7
def all_positive(numbers: list[int]) -> bool:
    for item in numbers:
        if item <= 0:
            return False
        else:
            return True

num = [1, 2, 3, -4]
print (all_positive(num))