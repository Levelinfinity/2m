# Task 1

def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_even(my_list))



# Task 2

def count_vowels(text):
    vowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"  
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

print(count_vowels("Привет World!"))



# Task 3

numbers_list = [1, 3, 5, 7, 10, 14, 15, 17, 20, 23, 25, 27, 30]


filtered_numbers = list(filter(lambda x: x % 5 == 0, numbers_list))

print(filtered_numbers)



# Task 4 

words = ["frontend", "backend", "fullstack"]

upper_words = list(map(lambda word: word.upper(), words))

print(upper_words)