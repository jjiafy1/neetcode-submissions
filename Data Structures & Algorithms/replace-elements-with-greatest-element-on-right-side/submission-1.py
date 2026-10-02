class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:    
    #Enhanced Solution Logic: Start at rightmost element, set it to the greatest value initially.
    #                         Traverse through the list moving left and check to see if the current element
    #                         is greater than the greatest value. If so, exchange values between greatest and
    #                         the current element value: set current element to what was the greatest.
    #                         Essentially, what this accomplishes is that each element starting from the right
    #                         is replaced with the largest value to the right of it, yet we keep the largest 
    #                         current value overall to compare against.
        greatestValue = 0

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > greatestValue:
                temp = arr[i]
                arr[i] = greatestValue
                greatestValue = temp
            else:
                arr[i] = greatestValue

        arr[len(arr) - 1] = -1
        
        return arr