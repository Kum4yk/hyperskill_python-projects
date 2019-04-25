class CoffeeMachine:
    def __init__(self):
        # default values
        self.__water_value = 1200
        self.__milk_value = 540
        self.__beans_value = 120
        self.__disposable_cups = 9
        self.__money = 550

    def __set_water(self, new_water: float):
        self.__water_value = new_water

    def __get_water(self):
        return self.__water_value

    def __set_mil(self, new_milk: float):
        self.__milk_value = new_milk

    def __get_milk(self):
        return self.__milk_value

    def __set_beans(self, new_beans: float):
        self.__beans_value = new_beans

    def __get_beans(self):
        return self.__beans_value

    def __set_cups(self, new_cups: float):
        self.__disposable_cups = new_cups

    def __get_cups(self):
        return self.__disposable_cups

    def __set_money(self, money: float):
        self.__money = money

    def __get_money(self):
        return self.__money

    def check_state(self):
        print(f"The coffee machine has:\n"
              f"{self.__get_water()} of water\n"
              f"{self.__get_milk()} of milk\n"
              f"{self.__get_beans()} of coffee beans\n"
              f"{self.__get_cups()} of disposable cups\n"
              f"{self.__get_money()} of money\n"
              )

    def buy_espresso(self):
        esp_water = 250
        esp_beans = 16
        esp_money = 4
        if self.__get_water() >= esp_water\
                and self.__get_beans() >= esp_beans\
                and self.__get_cups() > 0:
            self.__set_water(self.__get_water() - esp_water)
            self.__set_beans(self.__get_beans() - esp_beans)
            self.__set_money(self.__get_money() + esp_money)
            self.__set_cups(self.__get_cups() - 1)


if __name__ == "__main__":
    some = CoffeeMachine()
    some.check_state()
