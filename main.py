from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    pos_1 = 0
    pos_2 = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                pos_1 = i
                pos_2 = j
                break
    
    return [pos_1, pos_2]