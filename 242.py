class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        for cr in s:
            seen[cr] += 1
        
        for cr in t:
            seen[cr] -= 1
        
        for val in seen.values():
            if val != 0:
                return False
        
        return True