# check whether a no is prime or not

import math
num = 8

count = 0
for inc in range(2, math.floor(math.sqrt(num))):
    if num%inc == 0:
        count += 1
 
        
if count == 0:
    print('prime')
    
else:
    print('not prime')
    
