class SmartCalculator:
    @staticmethod
    def input_working():
        stop = "/exit"
        while True:
            values = input().rstrip()
            if values == stop:
                print("Bye!")
                break
            elif values == "/help":
                print("The program calculates the sum of numbers")
            elif values == '':
                continue
            print(SmartCalculator.string_handling(values))

    @staticmethod
    def string_handling(input_string):
        sign = 0
        result = 0
        for number in input_string.split():
            if number.isnumeric() or number[1:].isnumeric() or number[:-1].isnumeric():
                result += int(number) * (1 if sign % 2 == 0 else -1)
                sign = 0
            elif number[0] == '-':
                sign += len(number)
        return result


if __name__ == "__main__":
    SmartCalculator.input_working()
