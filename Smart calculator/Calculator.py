import operator
import numbers

class SmartCalculator:
    commands = {"/help", "/exit"}
    operations = {'-': 0, '+': 0, '*': 1, '/': 1, '^': 2}
    brackets = {'(', ')'}

    def __init__(self):
        self.run_state = True
        self.variables = dict()

    def do_command(self, command: str):
        if command == '/help':
            print("The program calculates the sum of numbers")
        elif command == "/exit":
            print("Bye!")
            self.run_state = False
        else:
            print("Unknown command")

    def __check_variable(self, variable):
        if variable not in self.variables:
            print("Unknown variable")
            return False
        return True

    @staticmethod
    def check_name(name: str):
        return any(let.isdigit() for let in name) and any(let.isalpha() for let in name)

    def assignment_variable(self, input_str: str):
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
            if not self.__check_variable(value):
                return None
            self.variables[name] = self.variables[value]

    def is_not_calculate(self, input_str: str):
        result = True
        if input_str == '':
            pass
        elif input_str[0] == "/":
            self.do_command(input_str)
        elif input_str.__contains__("="):
            self.assignment_variable(input_str)
        else:
            result = False
        return result

    @staticmethod
    def acts_with_brackets(brackets: list, value: str):
        if value == "(":
            brackets.append("(")
        elif value == ")":
            if len(brackets) == 0:
                print("Invalid expression")
                return True
            elif brackets[-1] == "(":
                brackets.pop()
        return False

    @staticmethod
    def __check_expression(expression):
        if expression[-1] in SmartCalculator.operations or expression[0] in {'*', '/', '^'}:
            print("Invalid expression")
            return True
        return False

    @staticmethod
    def __check_operation(current, previous, values, tack):
        if current in {'+', '-'} and previous in {'+', '-'} and not values:
            if current == "-":
                if previous == "-":
                    tack[-1] = '+'
                else:
                    tack[-1] = '-'
            return True
        elif previous in SmartCalculator.operations and not values:
            print("Invalid expression")
            return None
        return False

    def create_expression(self, input_str: str, is_eval=False):
        if SmartCalculator.__check_expression(input_str):
            return None
        input_str = input_str + "+"  # a little cheat for converting
        expr_by_list = [0] if input_str[0] in "-+" else []
        bracket_stack = list()
        current_value = ""

        for i in range(len(input_str)):
            elem = input_str[i]

            if elem == " ":
                continue

            elif elem in SmartCalculator.operations or elem in SmartCalculator.brackets:
                if elem in SmartCalculator.brackets\
                        and SmartCalculator.acts_with_brackets(bracket_stack, elem):
                    return None
                elif elem in SmartCalculator.operations:
                    prev = "___" if not expr_by_list else expr_by_list[-1]
                    checker = SmartCalculator.__check_operation(elem, prev, current_value, expr_by_list)
                    if checker:
                        continue
                    elif checker is None:
                        return None

                    if is_eval and elem == "^":
                        elem = "**"

                if current_value.isnumeric():
                    current_value = int(current_value)
                elif current_value.isalpha():
                    if not self.__check_variable(current_value):
                        return None
                    current_value = self.variables.get(current_value)

                if current_value or current_value == 0:  # we need number but 0 is a falsy value
                    expr_by_list.append(current_value)
                    current_value = ""
                expr_by_list.append(elem)
            else:
                current_value += elem

        if bracket_stack:
            print("Invalid expression")
            return None

        return expr_by_list[:-1]

    @staticmethod
    def to_postfix(expr):
        stack = list()
        output = list()

        for elem in expr:
            if isinstance(elem, numbers.Number):
                output.append(elem)
            elif elem in SmartCalculator.brackets:
                if elem == "(":
                    stack.append(elem)
                elif elem == ")":
                    value = stack.pop()
                    while not value == "(":
                        output.append(value)
                        value = stack.pop()
            else:
                while stack and stack[-1] in SmartCalculator.operations\
                        and SmartCalculator.operations[elem] <= SmartCalculator.operations[stack[-1]]:
                    output.append(stack.pop())
                stack.append(elem)

        while stack:
            output += stack.pop()
        return output

    @staticmethod
    def calculate_postfix(postfix):
        operations = {
            '+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': operator.truediv,
            '^': operator.pow
        }
        nums_stack = []
        operation_stack = []

        for token in postfix:
            if token not in SmartCalculator.operations:
                nums_stack.append(token)
            else:
                operation_stack.append(token)
                if nums_stack and operation_stack:
                    penultimate_token = nums_stack[-2]
                    last_token = nums_stack[-1]
                    math_sign = operation_stack[-1]
                    if last_token == 0 and math_sign == "/":
                        print('Division by zero!')
                        return None
                    res = operations[math_sign](penultimate_token, last_token)

                    nums_stack.pop()
                    nums_stack.pop()
                    operation_stack.pop()
                    nums_stack.append(res)
        return nums_stack[0]

    @staticmethod
    def __check_num(num):
        num = int(num) if float(num) - int(num) == 0 else float(num)
        return num

    @staticmethod
    def treatment_math_expression(expression: list, is_eval=False):
        if is_eval:
            try:
                answer = eval("".join(str(elem) for elem in expression))
                answer = SmartCalculator.__check_num(answer)
                print(answer)
            except ZeroDivisionError:
                print('Division by zero!')
        else:
            answer = SmartCalculator.calculate_postfix(
                SmartCalculator.to_postfix(
                    expression
                )
            )
            if answer is None:
                return None
            answer = SmartCalculator.__check_num(answer)
            print(answer)

    def main(self, is_eval=False):
        while self.run_state:
            values = input().strip()
            if self.is_not_calculate(values):
                continue

            result = self.create_expression(values)

            if result is None:
                continue

            SmartCalculator.treatment_math_expression(result, is_eval)


if __name__ == "__main__":
    SmartCalculator().main(False)
