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
        input_str = input_str + "+"  # a little cheat for calculate
        brackets = list()
        current_value = ""
        num_stack = [0]
        str_for_eval = ""

        for i in range(len(input_str)):

            elem = input_str[i]
            if elem == " ":
                continue
            elif elem in SmartCalculator.operations or elem == "(" or elem == ")":
                if elem == "(" or elem == ")":
                    if SmartCalculator.acts_with_brackets(brackets, elem):
                        print("Invalid expression")
                        return None
                else:
                    prev = input_str[i-1]
                    if prev == "*" or prev == "/" or prev == "^":
                        print("Invalid expression")
                        return None
                    if elem == "^":
                        elem = "**"

                if current_value.isnumeric():
                    num_stack.append(int(current_value))
                elif current_value.isalpha():
                    if self.variables.get(current_value, None) is None:
                        print("Unknown variable")
                        return None
                    num_stack.append(self.variables.get(current_value))
                    current_value = str(self.variables.get(current_value))

                str_for_eval += current_value + elem
                current_value = ""
            else:
                current_value += elem

        if brackets:
            print("Invalid expression")
            return None
        return str_for_eval[:-1], num_stack

    def main(self):
        while self.run_state:
            values = input().strip()
            if values == '':
                continue
            elif values[0] == "/":
                self.do_command(values)
                continue
            elif values.__contains__("="):
                self.assignment_variable(values)
                continue

            result = self.cheat(values)
            if result is None:
                continue
            else:
                result = eval(result[0])
                result = int(result) if float(result) - int(result) == 0 else result
                print(result)


if __name__ == "__main__":
    SmartCalculator().main()
