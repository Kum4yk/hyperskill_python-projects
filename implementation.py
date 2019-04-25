def __ingredient_for_coffee(needed_cups: float):
    """
    Now let's consider a case where you need a lot of coffee.
    One cup of coffee made on this coffee machine contains
     200 ml of water, 50 ml of milk, and 15 g of coffee beans.

    :param needed_cups: float ot inr type. Numbers of cups with coffee.
        Write how many cups of coffee you will need.
    :return: string. All ingredients number, ml and grams.
    """
    water_value = 200 * needed_cups
    milk_value = 50 * needed_cups
    beans_value = 15 * needed_cups

    return(f"For {needed_cups} cups you will need:\n"
           f"{water_value} ml of water\n"
           f"{milk_value} ml of milk\n"
           f"{beans_value} g of coffee beans")


def check_cups_from_ingredients(water_value: float,
                                milk_value: float,
                                beans_value: float,
                                needed_cups: float):

    milk_per_cup = 50
    water_per_cup = 200
    beans_per_cup = 15
    cups_list = list()

    cups_list.append(milk_value // milk_per_cup)
    cups_list.append(water_value // water_per_cup)
    cups_list.append(beans_value // beans_per_cup)

    possible_cups = min(cups_list)

    if needed_cups == possible_cups:
        return "Yes, I can make that amount of coffee"
    elif needed_cups > possible_cups:
        return f"No, I can make only {possible_cups} cups of coffee"
    else:
        return f"Yes, I can make that amount of coffee (and even { possible_cups - needed_cups} more than that)"


def __test_check_cups():
    print(check_cups_from_ingredients(300, 65, 100, 1))
    print(check_cups_from_ingredients(500, 250, 200, 10))
    print(check_cups_from_ingredients(1550, 299, 300, 3))
    print(check_cups_from_ingredients(0, 0, 0, 1))
    print(check_cups_from_ingredients(0, 0, 0, 0))
    print(check_cups_from_ingredients(200, 50, 15, 0))


def __hyperskill_check_cups():
    water_value = int(input("Write how many ml of water the coffee machine has: "))
    milk_value = int(input("Write how many ml of milk the coffee machine has: "))
    beans_value = int(input("Write how many grams of coffee beans the coffee machine has: "))
    needed_cups = int(input("Write how many cups of coffee you will need: "))
    print(check_cups_from_ingredients(water_value,
                                      milk_value,
                                      beans_value,
                                      needed_cups))


if __name__ == "__main__":
    __hyperskill_check_cups()
