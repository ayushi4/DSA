https://leetcode.com/problems/missing-number/

nums = [3,5,2,8,6,4,0,1]

#Gauss formula
#Time Complexity: O(n)
#Space Complexity: O(1)
exp_sum = len(nums)*(len(nums)+1)//2
acc_sum = 0

for i in nums:
    acc_sum += i
    
print(exp_sum-acc_sum)



#method-optimized: xor
#Time Complexity: O(n)
#Space Complexity: O(1)
ans = 0
for i in nums:
    ans = ans^i

for i in range(len(nums)+1):
    ans = ans^i

print(ans)
