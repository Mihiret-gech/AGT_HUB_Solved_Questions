class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hashmap = {}

        for i in range(len(nums)):
            current_num = nums[i]
            needed_number = target - current_num

            
            if needed_number in hashmap:
                previous_index = hashmap[needed_number]
               
                return [previous_index, i]

           
            hashmap[current_num] = i
