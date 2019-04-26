import copy


class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        # default values
        self.__water_value = copy.copy(water)
        self.__milk_value = copy.copy(milk)
        self.__beans_value = copy.copy(beans)
        self.__disposable_cups = copy.copy(cups)
        self.__money = copy.copy(money)

    def __set_water(self, new_water: int):
        self.__water_value = new_water

    def __get_water(self):
        return self.__water_value

    def __set_milk(self, new_milk: int):
        self.__milk_value = new_milk

    def __get_milk(self):
        return self.__milk_value

    def __set_beans(self, new_beans: int):
        self.__beans_value = new_beans

    def __get_beans(self):
        return self.__beans_value

    def __set_cups(self, new_cups: int):
        self.__disposable_cups = new_cups

    def __get_cups(self):
        return self.__disposable_cups

    def __set_money(self, money: int):
        self.__money = money

    def __get_money(self):
        return self.__money

    def __str__(self):
        return "The coffee machine has:\n" \
               "{0} of water\n" \
               "{1} of milk\n" \
               "{2} of coffee beans\n" \
               "{3} of disposable cups\n" \
               "{4} of money".format(self.__get_water(),
                                       self.__get_milk(),
                                       self.__get_beans(),
                                       self.__get_cups(),
                                       self.__get_money())

    def __add_fields(self, added_water=0,
                     added_milk=0, added_beans=0,
                     added_cups=0, added_money=0):

        self.__set_water(self.__get_water() + added_water)
        self.__set_milk(self.__get_money() + added_milk)
        self.__set_beans(self.__get_beans() + added_beans)
        self.__set_cups(self.__get_cups() + added_cups)
        self.__set_money(self.__get_money() + added_money)

    def __buy(self, needed_water, needed_milk,
              needed_beans, added_money):

        if self.__get_water() >= needed_water \
                and self.__get_beans() >= needed_beans \
                and self.__get_milk() >= needed_milk \
                and self.__get_cups() > 0:
            self.__add_fields(added_water=-needed_water,
                              added_milk=-needed_milk,
                              added_beans=-needed_beans,
                              added_cups=-1,
                              added_money=added_money)

    def buy_espresso(self):
        esp_water = 250
        esp_beans = 16
        esp_money = 4
        esp_milk = 0
        self.__buy(esp_water, esp_milk, esp_beans, esp_money)

    def buy_latte(self):
        lat_water = 350
        lat_milk = 75
        lat_beans = 20
        lat_money = 4
        self.__buy(lat_water, lat_milk, lat_beans, lat_money)

    def buy_cappuccino(self):
        cap_water = 200
        cap_milk = 100
        cap_beans = 12
        cap_money = 6
        self.__buy(cap_water, cap_milk, cap_beans, cap_money)

    def take(self):
        withdraw_money = self.__get_money()
        self.__set_money(0)
        return withdraw_money

    def hyperskill_test_stage4(self):
        buy_commands = {
            '1': self.buy_espresso(),
            '2': self.buy_latte(),
            '3': self.buy_cappuccino(),
            }

        action_command = {"buy", "fill", "take"}

        in_command = ""

        while in_command not in action_command:
            in_command = input("Write action (buy, fill, take): ").casefold()

        if in_command == "buy":
            while in_command not in buy_commands:
                in_command = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            buy_commands[in_command]
        elif in_command == "fill":
            water = int(input("Write how many ml of water do you want to add: "))
            milk = int(input("Write how many ml of milk do you want to add: "))
            coffee = int(input("Write how many grams of coffee beans do you want to add: "))
            cups = int(input("Write how many disposable cups of coffee do you want to add: "))
            self.__add_fields(added_water=water, added_milk=milk,
                              added_beans=coffee, added_cups=cups)
        elif in_command == "take":
            self.take()


if __name__ == "__main__":
    some = CoffeeMachine(1200, 540, 120, 9, 550)
    print(some)
    print()
    some.hyperskill_test_stage4()
    print()
    print(some)
