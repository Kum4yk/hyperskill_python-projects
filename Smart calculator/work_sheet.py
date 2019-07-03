class SmartCalculator:
    @staticmethod
    def sum_2_values():
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
            print(sum(map(int, values.split())))


if __name__ == "__main__":
    SmartCalculator.sum_2_values()
