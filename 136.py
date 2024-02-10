class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash map record show num
        show = set()
        # if show, remove it
        # after iterate all element, only one ele left in show
        for i in nums:
            if i not in show:
                show.add(i)
            else:
                show.remove(i)
        show = list(show)
        return show[0]