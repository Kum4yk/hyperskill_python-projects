class SmartCalculator:
    commands = {"/help", "/exit"}
    operations = {'-': 0, '+': 0, '*': 1, '/': 1, '^': 2}

    def __init__(self):
        self.run_state = True
        self.variables = dict()

    def do_command(self, command):
        if command == '/help':
            print("The program calculates the sum of numbers")
        elif command == "/exit":
            print("Bye!")
            self.run_state = False
        else:
            print("Unknown command")

    @staticmethod
    def check_name(name):
        return any(let.isdigit() for let in name) and any(let.isalpha() for let in name)

    def assignment_variable(self, input_str):
        i = input_str.index("=")
        name = input_str[:i].strip()
        value = input_str[i+1:].strip()
        if SmartCalculator.check_name(name):
            print("Invalid identifier")
            return None
        elif SmartCalculator.check_name(value) or input_str.count("=") != 1:
            print("Invalid assignment")
            return None
        elif value.isnumeric():
            self.variables[name] = int(value)
        else:
            if value not in self.variables:
                print("Unknown variable")
                return None
            self.variables[name] = self.variables[value]

    def main(self):
        while self.run_state:
            values = input().rstrip()
            if values == '':
                continue
            elif values[0] == "/":
                self.do_command(values)
                continue
            elif values.__contains__("="):
                self.assignment_variable(values)
                continue
            elif values.count("-") == 0 and values.count("+") == 0:
                print(self.variables.get(values.strip(), "Unknown variable"))
                continue
            values = values.split()
            print(self.string_handling(values))

    def string_handling(self, input_string: list):
        wait_number = True
        sign = 0
        result = 0
        for number in input_string:
            if wait_number:
                wait_number = False
                sign = (1 if sign % 2 == 0 else -1)
                if number in self.variables:
                    result += self.variables[number] * sign
                else:
                    try:
                        result += int(number) * sign
                    except ValueError:
                        return "Invalid expression"
                sign = 0
            else:
                wait_number = True
                if number[0] == '-':
                    sign += len(number)
                elif number[0] == "+":
                    continue
                else:
                    return "Invalid expression"
        return result

    @staticmethod
    def acts_with_brackets(brackets: list, value: str):
        result_is_bad = False
        if value == "(":
            brackets.append("(")
        elif value == ")":
            if len(brackets) == 0:
                result_is_bad = True
            elif brackets[-1] == "(":
                brackets.pop()
        return result_is_bad

    def cheat(self, input_str: str):
        brackets = list()
        prev_is_num = False
        current_value = ""
        num_stack = [0]

        for i in range(len(input_str)):
            elem = input_str[i]
            if elem == " ":
                if prev_is_num:
                    num_stack.append(int(current_value))
                else:
                    if current_value not in self.variables:
                        print("Unknown variable")
                        break
                    num_stack.append(self.variables[current_value])
                current_value = ""
                continue
            elif elem == "(" or elem == ")":
                if SmartCalculator.acts_with_brackets(brackets, elem):
                    print("Invalid expression")
                    break
            elif elem in SmartCalculator.operations or elem == "(" or elem == ")":
                if current_value.isalpha():
                    pass

            elif elem.isdigit():
                if prev_is_num:
                    current_value += elem
                else:
                    current_value = elem
                prev_is_num = True
            elif elem.isalpha():
                if prev_is_num:
                    current_value = elem
                else:
                    current_value += elem
                prev_is_num = False
        if not brackets:
            print("Invalid expression")

    def calculate_input(self, input_str: str):
        operations_stack = list()
        polish_notation = list()
        brackets = list()
        wait_number = True
        sign = 0  # val if sign % 2 == 0 else -val
        prev_is_num = False
        for elem in input_str:
            if elem == " ":
                continue


if __name__ == "__main__":
    SmartCalculator().main()

