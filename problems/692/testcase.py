from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["i", "love", "leetcode", "i", "love", "coding"], 2), Output=["i", "love"]))
        self.testcases.append(case(Input=(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
                                   Output=["the", "is", "sunny", "day"]))

    def get_testcases(self):
        return self.testcases
