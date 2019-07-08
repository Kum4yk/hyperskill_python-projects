def check_order(numbers):
    ascending_order = True
    descending_order = True
    if len(numbers) == 0 or len(numbers) == 1:
        return True
    first = numbers[0]
    i = 1
    while (ascending_order or descending_order) and i < len(numbers):
        if numbers[i] > first:
            descending_order = False
        if numbers[i] < first:
            ascending_order = False
        first = numbers[i]
        i += 1
    return ascending_order or descending_order


def vowels_consonants(word):
    vowels = set('eyuioa')
    consonants = set('qwrtpsdfghjklzxcvbnm')
    for letter in word:
        if letter in vowels:
            print("vowel")
        elif letter in consonants:
            print("consonant")
        else:
            break


def unique_subjects(dictionary):
    result = set()
    for key in dictionary:
        result = result.union(set(dictionary[key]))
    return len(result)


def read_unique():
    words = list()
    for i in range(10):
        words += input().split()
    unique = set(words)
    print(unique, len(unique))
    print(words, len(words))
    return round(len(unique) / len(words) * 100)


if __name__ == "__main__":
    value = read_unique()
    if value <= 20:
        print(1)
    elif 21 <= value <= 40:
        print(2)
    elif 41 <= value <= 60:
        print(3)
    elif 61 <= value <= 80:
        print(4)
    else:
        print(5)
