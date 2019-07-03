def hand_cards():
    some_d = {"Jack": 11,
              "Queen": 12,
              "King": 13,
              "Ace": 14}

    in_str = input().split()
    # print(in_str)
    all_sum = 0

    for i in range(len(in_str)):
        if in_str[i] in some_d:
            all_sum += some_d[in_str[i]]
            in_str[i] = some_d[in_str[i]]
        else:
            all_sum += int(in_str[i])
            in_str[i] = int(in_str[i])
    in_str.sort()

    if [2, 3, 4, 5] == in_str[:4] and in_str[-1] == 14:
        all_sum -= 13
    value = round(all_sum / len(in_str), 2)
    print('{:.2f}'.format(value))


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
        for ingr in some:
            if ingr.startswith(name):
                print("You can make", book_name[i])
        i = (i + 1) % 5


if __name__ == '__main__':
    print(asdvc)

