class SmartCalculator:
    operations = {'+', '-', '='}

    def __init__(self):
        self.variables = dict()

    @staticmethod
    def main():
        while True:
            values = input().rstrip()
            if values == '':
                continue
            if values[0] == "/":
                if values == '/help':
                    print("The program calculates the sum of numbers")
                elif values == "/exit":
                    print("Bye!")
                    break
                else:
                    print("Unknown command")
                continue
            print(SmartCalculator.string_handling(values))
    ''.count()
    @staticmethod
    def string_handling(input_string):
        wait_number = True
        sign = 0
        result = 0
        for number in input_string.split():
            if wait_number:
                try:
                    result += int(number) * (1 if sign % 2 == 0 else -1)
                except ValueError:
                    return "Invalid expression"
                sign = 0
                wait_number = False
            else:
                wait_number = True
                if number[0] in SmartCalculator.operations:
                    if number[0] == '-':
                        sign += len(number)
                else:
                    return "Invalid expression"
        return result


if __name__ == "__main__":
    new = SmartCalculator()
    new.main()


