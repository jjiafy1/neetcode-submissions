class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:    
# Base logic: start with current element (i), traverse down the right and keep track of what the largest value is.
#             If one element is found to be greater than the previous largest, make this value the new largest.
#             Then, replace current element with largest value and move one element to the right to repeat.

        for i in range(len(arr)):
            greatestElement = 0
            for j in range(i + 1, len(arr)):
                if arr[j] > greatestElement:
                    greatestElement = arr[j]
            arr[i] = greatestElement
        
        arr[len(arr) - 1] = -1

        return arr;