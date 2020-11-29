# will work if we consider we have infinite no of supplies of each item
# weight array and value array to maximize profit, within the capacity of knapsack
wt = [1,3,4,5]
val = [1,4,5,7]
W = 7
# n = len(wt)
d = {}
for i in range(len(wt)):
    d[wt[i]] = val[i]     #hash-map to store wt and val
print(d)
# d = {
#     1:1,
#     3:4,
#     4:5,
#     5:7
# }
def knapsack(wt, val, W, d):
    print(W)
    if W==0:      #base condition 
        return 0
    
    
    if W in d:    # use of memoization to optimize time complexity
        return d[W]
    max_p = -10**9  
    for w in wt:
        if w <= W:
            ans = knapsack(wt, val, W-w, d) + d[w]
            max_p = max(max_p, ans)
            # return max_p
        # if w > W:
        # else:
        #     max_p = knapsack(wt, val, W)
    # return max_p
            
    d[w] = max_p   #memoization
    return max_p
    
max_profit =  knapsack(wt, val, W, d)
print('-'*20)
print(max_profit)
