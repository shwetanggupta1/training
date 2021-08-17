
from collections import Counter

list1=[3,4,1,6,4,2,7,8,7]

print([x for x, count in Counter(list1).items() if count>1])
