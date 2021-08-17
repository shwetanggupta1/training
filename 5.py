from itertools import permutations
def largest(n):
    list1 = []
    for i in permutations(n, len(n)):
        list1.append(''.join(map(str,i)))
    return max(list1)
 
print(largest([3,8,5,9,98,101]))
