class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # initialize a stack
        stack = [] # survive asteroid

        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                # Handling collision with negative asteroid, use while to check all the ast in stack
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop()
                # if all ast is negetive
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                # edgw case
                elif stack[-1] == -ast:
                    stack.pop()
        
        return stack