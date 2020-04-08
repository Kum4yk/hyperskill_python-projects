import argparse
import math


class CreditCalculator:
    def __init__(self, calc_type, principal, periods, interest, payment):
        self.type = calc_type
        self.principal = principal
        self.periods = periods
        self.interest = None if interest is None else interest / (100 * 12)
        self.payment = payment

    def __calc_additional(self):
        return self.interest * (1 + self.interest) ** self.periods / ((1 + self.interest) ** self.periods - 1)

    def __calc_periods(self):
        self.periods = math.ceil(
            math.log(
                self.payment / (self.payment - self.interest * self.principal),
                self.interest + 1
            )
        )
        y, m = self.periods // 12, self.periods % 12
        y_s, m_s = ["s" if x > 1 else "" for x in (y, m)]

        m = f" {m} month{m_s}" if m else ""
        y = f"{y} year{y_s}" + " and" * bool(m) if y else ""

        overpayment = self.payment * self.periods - self.principal

        return f"You need {y}{m} to repay this credit!\nOverpayment = {overpayment}"

    def __calc_diff_payment(self):
        all_payments = 0
        for i in range(1, self.periods + 1):
            diff_pay = math.ceil(
                self.principal / self.periods + self.interest *
                (self.principal - self.principal * (i - 1) / self.periods)
            )
            all_payments += diff_pay
            print(f"Month {i}: paid out {diff_pay}")
        print()
        overpayment = all_payments - self.principal
        return f"Overpayment = {overpayment}"

    def __calc_payment(self):
        self.payment = math.ceil(
            self.principal * self.__calc_additional()
        )
        overpayment = self.payment * self.periods - self.principal

        return f"Your annuity payment = {self.payment}!\nOverpayment = {overpayment}"

    def __calc_principal(self):
        self.principal = int(self.payment / self.__calc_additional())
        overpayment = self.periods * self.payment - self.principal

        return f"Your credit principal = {self.principal}!\nOverpayment = {overpayment}"

    def do_calc(self):
        if self.periods is None:
            return self.__calc_periods()
        if self.principal is None:
            return self.__calc_principal()
        if self.payment is None:
            if self.type == "diff":
                return self.__calc_diff_payment()
            return self.__calc_payment()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=int)

    args = parser.parse_args()
    lst = [args.type, args.principal, args.periods, args.interest, args.payment]
    if lst.count(None) != 1 or lst[3] is None:
        print("Incorrect parameters.")
    else:
        credit_calc = CreditCalculator(*lst)
        print(credit_calc.do_calc())
