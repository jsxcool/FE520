def removeDuplicates(nums):
        if nums == []:
            return 0
        
        length = len(nums)
        newIndex = 0
        for i in range(length-1):
            if(nums[i] != nums[i+1]):
                newIndex += 1
                nums[newIndex] = nums[i+1]
        return newIndex+1
        
 
ls = [1,2,2,3,3,4,5]
print(removeDuplicates(ls))
