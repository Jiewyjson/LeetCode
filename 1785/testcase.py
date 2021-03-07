from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1,-1,1], 3, -4), Output=2))
        self.testcases.append(case(Input=([1,-10,9,1],100, 0), Output=1))

    def get_testcases(self):
        return self.testcases
