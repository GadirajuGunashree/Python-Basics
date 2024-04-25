# SELECTION SORT
def performSelectionSort(nums):
    n = len(nums)
    for fixThisIndex in range(n - 1, 0, -1):
        maxEle = nums[fixThisIndex]
        maxEleIndex = fixThisIndex 

        for index in range(fixThisIndex):
            if nums[index] > maxEle:
                maxEleIndex = index 
                maxEle = nums[index]
        if fixThisIndex != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp

        print(nums)

nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]

print("Before sorting:")
print(nums) 
performSelectionSort(nums)

print("After sorting:")
print(nums)

#INSERTION SORT
def performInsertionSort(nums):
    n = len(nums)
    for index in range(1, n):
        temp = nums[index]
        position = index - 1 
        while position >= 0 and nums[position] > temp:
            nums[position + 1] = nums[position]
            position -= 1 

        nums[position + 1] = temp 
        print(nums)

nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]

print("Before sorting:")
print(nums)
performInsertionSort(nums)
print("After sorting:")
print(nums)
