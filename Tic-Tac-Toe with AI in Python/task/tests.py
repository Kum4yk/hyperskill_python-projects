from hstest.stage_test import *
from hstest.test_case import TestCase
import re


class TicTacToeTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply: str, attach: str) -> CheckResult:
        reply = re.sub("\\s+", "", reply)
        if len(reply) > 9:
            return CheckResult(False, "You need to output no more than 9 symbols")
        have_x = False
        have_o = False
        for c in reply:
            if c != 'X' and c != 'O':
                return CheckResult(False, "You need to output X and O " + "symbols only not counting spaces")
            if c == 'X':
                have_x = True
            if c == 'O':
                have_o = True
        if not have_x:
            return CheckResult.false("You need to output at least one X")
        if not have_o:
            return CheckResult.false("You need to output at least one O")
        return CheckResult.true()


if __name__ == '__main__':
    TicTacToeTest('tictactoe.tictactoe').run_tests()
