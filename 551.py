class Solution:
    def checkRecord(self, s: str) -> bool:
        # Absent for strictly fewer than 2 days total(<2)
        # late for 3 or more consecutive days(>=3)
        absent = []
        for i in range(len(s)):
            # check abent condition
            if s[i] == 'A':
                absent.append(s[i])
                if len(absent) >= 2:
                    return False
            # check late condition
            elif s[i] == 'L':
                if i + 2 < len(s):
                    if s[i + 1] == 'L' and s[i + 2] == 'L':
                        return False
        
        return True