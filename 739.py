class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize a stack, pair: [temp, index]
        # the number of days have to wait will be index - index
        # initialize result
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        # enumerate will get the index and value at the same time
        for i, t in enumerate(temperatures):
            # check if stack is empty and this temp greater than the temp on the top of our stack
            # the top of the stack index is -1, and the temp index in pair is 0
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # update the result, the stackInd is the cooler temp, i is the warmer temp first meet
                res[stackInd] = (i - stackInd)
            stack.append([t, i])

        return res