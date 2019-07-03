animal_list = [['chicken', 23],
               ['dog', 137],
               ['goat', 678],
               ['pig', 1296],
               ['cow', 3848],
               ['Sheep', 6769]]
animal_list.sort(key=lambda x: x[1], reverse=True)
none_flag = True

money = int(input())
for name, price in animal_list:
    if money // price <= 0:
        continue
    else:
        print(money // price,
              " " + name,
              's' if money // price > 1 else '',
              sep='', end='')
        none_flag = False
        break
if none_flag:
    print("None")
