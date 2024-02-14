class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        split_s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                # if current char is ( then push it to stack
                # record the index
                stack.append(i)
            elif s[i] == ')':
                # if current char is ), then pop the top of the stack
                if len(stack) != 0:
                    stack.pop()
                else:
                # if stack are empty, can't pop so make current char as ''
                    split_s[i] = ''

        # any char left in stack need to be remove
        for i in stack:
            split_s[i] = ''

        return ''.join(split_s)