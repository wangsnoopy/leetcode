class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # a record stack to record the score
        # interate all the ele in ops
        record = []
        for i in operations:
            if i == '+':
                score = record[-1] + record[-2]
                record.append(score)
            elif i == 'C':
                record.pop()
            elif i == 'D':
                score = record[-1] * 2
                record.append(score)
            # if i is num, record i
            else:
                record.append(int(i))

        return sum(record)
    