import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        operations, sources = test_input
        iter_ = PeekingIterator(Iterator(list(sources[0]).pop()))
        ans = [None]
        for i in range(1, len(operations)):
            if operations[i] == "next":
                res = iter_.next()
            elif operations[i] == "peek":
                res = iter_.peek()
            else:
                res = iter_.hasNext()
            ans.append(res)
        return ans


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        # self.nothing can be replaced by a boolean variable that mark has_peek or not
        self.nothing = []
        self.peek_element = self.nothing

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_element != self.nothing:
            return self.peek_element
        if self.iterator.hasNext():
            self.peek_element = self.iterator.next()
        return self.peek_element

    def next(self):
        """
        :rtype: int
        """
        if self.peek_element != self.nothing:
            val = self.peek_element
            self.peek_element = self.nothing
            return val
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peek_element != self.nothing or self.iterator.hasNext()


# Below is the interface for Iterator, which is already defined for you.
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.index = 0
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        assert self.hasNext()
        obj = self.nums[self.index]
        self.index += 1
        return obj
