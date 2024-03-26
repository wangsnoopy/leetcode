class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # for nums = [1,2,3] k=3, the sub array is 1,2 and 3
        # all subarray can calculate by sum(0,x) - sum(0,y)
        # initialze the HashMap = {0:1}
        # for each number x in array, sum += x
        # if sum - k is in map -> result += HashMap[sum - k]
        # put sum into the map, or increase it count if exists
        sum_num, result = 0, 0
        seen = {0:1}
        for x in nums:
            sum_num += x
            if sum_num - k in seen:
                result += seen[sum_num - k]
            if sum_num not in seen:
                seen[sum_num] = 1
            elif sum_num in seen:
                seen[sum_num] += 1
        
        return result