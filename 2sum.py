from collections import defaultdict
nums = [2,7,11,15]            
target = 9

#bf alg of O(n^2)
def twoSumBruteforce(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
ansBF = twoSumBruteforce(nums,  target)
# print(ansBF)

# optimal with O(n)
def twoSumOptimal(nums, target):
    diff = defaultdict(int)
    for i in range(len(nums)):
        diff[nums[i]] = i
    for i in range(len(nums)):
        comp = target-nums[i]
        if comp in diff and diff[comp] != i:
            return [i , diff[comp]]

ansOp = twoSumOptimal(nums,target)
print(ansOp)
