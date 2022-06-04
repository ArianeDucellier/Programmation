class MinStack(object):

    def __init__(self):
        self.min_stack = None
        self.list_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.list_stack.append(val)
        if val < self.min_stack:
            self.min_stack = val

    def pop(self):
        """
        :rtype: None
        """
        value = self.list_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return list_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack
