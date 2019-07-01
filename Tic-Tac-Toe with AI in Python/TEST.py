def farm():
    animal_list = [['Chicken', 23],
                   ['Dog', 137],
                   ['Goat', 678],
                   ['Pig', 1296],
                   ['Cow', 3848],
                   ['Sheep', 6769]]
    animal_list.sort(key=lambda x: x[1], reverse=True)
    none_flag = True

    money = int(input())
    for name, price in animal_list:
        if money // price < 1:
            continue
        else:
            print(money // price,
                  " " + name.lower(),
                  's' if money // price > 1 else '',
                  sep='')
            none_flag = False
            break
    if none_flag:
        print("None")


def morphology():
    roots = input().split()
    affixes = input().split()
    word = input()
    is_word = False
    for root in roots:
        if word.startswith(root):
            for suffix in affixes:
                if word == root + suffix:
                    is_word = True
                    break
        elif word.endswith(root):
            for prefix in affixes:
                if word == prefix + root:
                    is_word = True
                    break
    if is_word:
        print("It is a word")
    else:
        print("It is not a word")


def cook_book():
    pasta = set("tomato, basil, garlic, salt, pasta, olive oil".split(', '))
    apple_pie = set("apple, sugar, salt, cinnamon, flour, egg, butter".split(', '))
    ratatouille = set("eggplant, carrot, onion, tomato, garlic, olive oil, pepper, salt".split(', '))
    chocolate_cake = set("chocolate, sugar, salt, flour, coffee, butter".split(', '))
    omelette = set("egg, milk, bacon, tomato, salt, pepper".split(', '))

    book = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
    book_name = ['pasta', "apple pie", "ratatouille", "chocolate cake", "omelette"]
    # sort_book_name = ['apple pie', 'chocolate cake', 'omelette', 'pasta', 'ratatouille']
    # sort_book = [apple_pie, chocolate_cake, omelette, pasta, ratatouille]

    # print(sort_book)
    name = input()
    i = 0
    for some in book:
        print(some)
        if name in some:
            print("You can make", book_name[i])
        i = (i + 1) % 5


if __name__ == "__main__":
    cook_book()
