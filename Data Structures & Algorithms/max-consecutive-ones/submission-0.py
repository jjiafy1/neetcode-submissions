class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxOnes = 0
        tempMax = 0

        # Iterate through the array and keep a temporary count per consecutive 1s
        for i in range(0, len(nums)):
            # Increment temp 1s count if current element is a 1
            if nums[i] == 1:
                tempMax+=1
            # Otherwise, if element is 0, then check if the current/temp count is greater than the all time max
            else:
                if tempMax > maxOnes:
                    maxOnes = tempMax
                    tempMax = 0
                else:
                    tempMax = 0
        
        # If final element is a 1, then check if the current/temp count is greater than the all time max
        if (tempMax > maxOnes):
            maxOnes = tempMax
        
        return maxOnes

        