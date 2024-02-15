class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # remove the outer parenthess
        # first ( meet the first ), keep thing inside
        # stack to record the index
        # let s be a list
        # interate all index and final remove the outer index
        see = []
        remove_p = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == '(':
                see.append(i)
            else:
                # there is only one ( in remove, that means there are the outer, record in remove
                if len(see) == 1:
                    remove_p.append(see.pop())
                    remove_p.append(i)
                else:
                    see.pop()
        # remove the outer
        for j in remove_p:
            s_list[j] = ''
        
        return ''.join(s_list)