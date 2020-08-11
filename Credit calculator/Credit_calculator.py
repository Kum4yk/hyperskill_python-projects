import argparse
import math
import numbers


class CreditCalculator:
    def __init__(self,interest, calc_type, principal, periods, payment):
        self.type = calc_type
        self.principal = principal
        self.periods = periods
        self.interest = interest if interest is None else interest / (100 * 12)
        self.payment = payment
        self.overpayment = 0

    def __calc_additional(self):
        return self.interest * (1 + self.interest) ** self.periods / ((1 + self.interest) ** self.periods - 1)

    def __calc_overpayment(self, all_payment=0):
        if self.type == "diff":
            return all_payment - self.principal
        return self.payment * self.periods - self.principal

    def __calc_periods(self):
        self.periods = math.ceil(
            math.log(
                self.payment / (self.payment - self.interest * self.principal),
                self.interest + 1
            )
        )
        years, months = self.periods // 12, self.periods % 12
        year_end, month_end = ["s" if x > 1 else "" for x in (years, months)]
        months = f" {months} month{month_end}" if months else ""
        years = f"{years} year{year_end}" + " and" * bool(months) if years else ""

        self.overpayment = self.__calc_overpayment()
        return f"You need {years}{months} to repay this credit!\nOverpayment = {self.overpayment}"

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

        self.overpayment = self.__calc_overpayment(all_payments)
        return f"Overpayment = {self.overpayment}"

    def __calc_payment(self):
        self.payment = math.ceil(
            self.principal * self.__calc_additional()
        )
        self.overpayment = self.__calc_overpayment()
        return f"Your annuity payment = {self.payment}!\nOverpayment = {self.overpayment}"

    def __calc_principal(self):
        self.principal = int(self.payment / self.__calc_additional())
        self.overpayment = self.__calc_overpayment()
        return f"Your credit principal = {self.principal}!\nOverpayment = {self.overpayment}"

    def check_state(self):
        lst = [self.type, self.principal, self.periods, self.payment]
        if self.interest is None or lst.count(None) != 1 or \
                any([elem < 0 for elem in lst if isinstance(elem, numbers.Number)]):
            return False
        return True

    def do_calc(self):
        if not self.check_state():
            return "Incorrect parameters."

        if self.periods is None:
            return self.__calc_periods()
        if self.principal is None:
            return self.__calc_principal()
        if self.payment is None:
            if self.type == "diff":
                return self.__calc_diff_payment()
            return self.__calc_payment()

        return "Impossible output by task condition!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=int)

    args = parser.parse_args()
    params = [args.interest, args.type, args.principal,
              args.periods, args.payment]

    credit_calc = CreditCalculator(*params)

    print(credit_calc.do_calc())

