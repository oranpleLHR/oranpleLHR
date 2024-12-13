#1
def greet(name: str) -> str:
    return f"hello {name}!"

user_name = input("type your name here: ")
print(greet(user_name))

#2
def square_numbers(numbers: list[int]) -> list[int]:
    return [num ** 2 for num in numbers]

given_num = input("give a list of numbers here, seperate by,: ")
numbers = [int(num.strip()) for num in given_num.split(",")]
print(f"the squares of the numbers in the list are: {square_numbers(numbers)}")

#3
def remove_item(item: list[str], item_to_remove: str) -> list[str]:
    return [item for item in item if item != item_to_remove]

item = ["283", "707", "150"]
print(item)

item_to_remove = input("Type the item to be removed: ").strip()

result = remove_item(item, item_to_remove)
print (f"Updated list: {result}")