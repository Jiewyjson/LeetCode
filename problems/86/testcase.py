from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 3, 2, 5, 2], 3], Output=[1, 2, 2, 4, 3, 5]))
		self.testcases.append(case(Input=[[2, 1], 2], Output=[1, 2]))

	def get_testcases(self):
		return self.testcases
