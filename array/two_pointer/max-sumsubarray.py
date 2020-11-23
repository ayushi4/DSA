
#without using two-pointer(sliding window)

arr = [2,5,10,8,2,9,1]
k = 3


sum = 0
for i in range(k):
    sum += arr[i]
    
mx = sum
for i in range(k, len(arr)):
    
    sum = sum + arr[i] - arr[i-k]
    
    if mx<sum:
        mx = max(mx, sum)
        
    
print(mx)
        
