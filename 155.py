class MinStack:

    def __init__(self):
        # one stack to record
        # one stack to find the min val
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if current val is min, add to min stack
        if len(self.min) == 0 or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        # if pop val == minnest val in min, pop it
        if self.top() == self.min[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]