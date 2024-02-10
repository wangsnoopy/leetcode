class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # dic to record ele show in s
        show = {}
        for ele in s:
            if ele not in show:
                show[ele] = 1
            # if show, + 1
            else:
                show[ele] += 1
        # count the ele show time, if show in t, - 1
        # Iterate t
        for i in t:
            if i in show:
                if show[i] > 0:
                    show[i] -= 1
                else:
                    return False
            else:
                return False
        return True