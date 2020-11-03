#using union find

def find(a):
    if a == link[a]:
        return a
    return find(link[a])

def merge(a, b):
    a = find(a)   # 3
    b = find(b)   # 2
    if size[a] < size[b]:  # size[3] < size[2]
        a, b = b, a      #  a, b = 3,2--> 2,3
      
    link[b] = link[a]  
    size[a] += size[b]
    
def same(a, b):
    if find(a) == find(b):
        return True
    return False

edges=[
    [0, 2, 7],
    [2, 4, 1],  1
    [3, 4, 5],  4
    [3, 1, 4],  3
    [2, 1, 8],
    [0, 4, 3]   2
]   
    #   0, 1, 2, 3, 4
link = [2, 3, 2, 2, 2]
size = [1, 1, 5, 2, 1]

edges.sort(key=lambda x:x[2])
result = []
for edge in edges:
    if same(edge[0], edge[1]):
        continue
    
    merge(edge[0], edge[1])
    result.append(edge)
    
print(result)
