from collections import Counter

def nonrpt(string):
    a=Counter(string)
    for i in string:
        if (a[i]==1):
            print(i)
            break


string='abbcd'
nonrpt(string)
