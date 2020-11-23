#sum of n fibonacci numbers

count = 0
def fib(n, d):
    
    global count 
    count += 1
    # print(n)
    
    if n in d:
        return d[n]
        
    ans = fib(n-1, d) + fib(n-2, d)
    d[n] = ans 
    return ans
    

d={}    
d[0] = 0
d[1] = 1
print('-'*20)
ans = fib(10, d)
# res = fib(5)
print(ans)
print(count)
