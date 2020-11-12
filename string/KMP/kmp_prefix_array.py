str = "acacabacacabacacac" 
#"abcaby"
i = 1
j = 0



p_arr = [0]*len(str)

while(i<len(str)):
    if str[i] != str[j]:
        if j!=0:
            j = j - 1
            j = p_arr[j]
            
        if j == 0:
            p_arr[i] = j
            i = i + 1
    elif str[i] == str[j]:
        j = j + 1
        p_arr[i] = j
        i = i + 1
        
print(p_arr)

#"a b c a b y"
#[0, 0, 0, 1, 2, 0]
# a  c  a  c  a  b  a  c  a  c  a  b  a  c  a  c   a   c
#[0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 4]
