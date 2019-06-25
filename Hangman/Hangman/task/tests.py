from hstest.stage_test import *
from hstest.test_case import TestCase


right_str = """H A N G M A N
The game will be available soon."""


class CoffeeMachineTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(attach=right_str)]

    def check(self, reply: str, attach: str) -> CheckResult:
        if reply.strip() == attach.strip():
            return CheckResult.true()
        return CheckResult.false(
            "You should print output exactly like in the example")


if __name__ == '__main__':
    CoffeeMachineTest('hangman.hangman').run_tests()
