https://leetcode.com/problems/missing-number/

#Gauss formula
nums = [3,5,2,8,6,4,0,1]
        
exp_sum = len(nums)*(len(nums)+1)//2
acc_sum = 0

for i in nums:
    acc_sum += i
    
print(exp_sum-acc_sum)
