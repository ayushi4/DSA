# without memoization

wt = [1,3,4,5]
val = [1,4,5,7]
W = 10
n = len(wt)

def knapsack(wt, val, W, n):
    # print(W)
    if W==0 or n==0:
        return 0
        
    if wt[n-1]<=W:
        return max(val[n-1]+ knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
    elif wt[n-1]>W:
        return knapsack(wt, val, W, n-1)
     
     
    
max_profit =  knapsack(wt, val, W, n)
print('-'*20)
print(max_profit)

# W=7, o/p= 9
# W=10, o/p= 13
