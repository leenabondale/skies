class Solution:
    
    # input nums: [1, 3, 4, 5, 6], target=7
    # output: [3, 4]
    # def twoSum2(self, nums: List[int], target: int) -> List[int]:
    #     output: List[int]
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if nums[i]+nums[j] == target:
    #                 output = [i, j]
    #                 return output
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output: List[int]
        p1 = 0
        p2 = 1
        while p1 < len(nums) | p2 < len(nums):
            value = nums[p1] + nums[p2]
            print('value: {0} and target: {1}'.format(value, target))
            if value == target:
                output = [p1, p2]
                return output
            elif value < target:
                p2=p2+1
            else:
                p1=p1+1
                    
                    
                    
        
