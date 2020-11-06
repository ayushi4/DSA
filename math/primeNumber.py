# find all prime numbers from 1 to given number

import math
num = 100

inc = 2
result = []
while (inc!=num):
    
    count = 0
    for k in range(2, math.floor(math.sqrt(inc))+1):
        if inc%k == 0:
            count += 1
            
            
    if count == 0:
        result.append(inc)
    
    
    inc += 1
    
print(result)
