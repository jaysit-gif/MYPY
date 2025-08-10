from s import sort 
from lnm import A #when i was working on this i used the lnm file to them the code
from lnm import A1


def oldbinary_search(B,target):
    B = sort(B,"asc")
    low = 0
    high = len(B)-1
    while low<=high:
        mid = (low+high)//2
        if target == B[mid]:
            return mid
        elif target > B[mid]:
            low = mid - 1
        elif target < B[mid]:
            high = mid + 1

    return -1        

def linear_search(B,target):
    for i in range(0,len(B)):
        if B[i] == target:
            return i
    return -1    

def binary_search(B,target):
    sort_B = sort(B[:],"asc")
    low = 0
    high = len(sort_B)-1
    while low<=high:
        mid = (low+high)//2
        if target == sort_B[mid]:
            return mid,sort_B
        elif target > sort_B[mid]:
            low = mid + 1
        elif target < sort_B[mid]:
            high = mid - 1

    return -1,sort_B       

def visualbinary_search(B, target):
    sort_B = sort(B[:], "asc")
    low = 0
    high = len(sort_B) - 1
    step = 0

    print(f"Searching for {target} in:")
    print(sort_B)
    print("-" * 40)

    while low <= high:
        mid = (low + high) // 2
        print(f"Step {step}:")
        print(f"  low={low}, high={high}, mid={mid}")
        print(f"  Comparing {target} to sort_B[{mid}] = {sort_B[mid]}")
        
        if target == sort_B[mid]:
            print(f"  ➤ Found at index {mid}")
            return mid, sort_B
        elif target > sort_B[mid]:
            low = mid + 1
        else:
            high = mid - 1
        step += 1
        print("-" * 40)

    print(f"  ➤ {target} not found.")
    return -1, sort_B  


def lfindmax(B):
    B_sort = sort(B,"desc")
    return B_sort[0]

def findmean(B):
    n = len(B)
    k = 0
    for i in range(len(B)):
        k += B[i]
    return k/n    

def find_distinct_elements(B):
    l = []
    sort_B = sort(B[:],"asc")
    a = len(sort_B)
    for i in range(a-1):
        if sort_B[i] != sort_B[i+1]:
            l.append(sort_B[i])

    l.append(sort_B[a-1])

    return l

def findfreq(B,k):
    u = 0
    a = len(B)
    for i in range(a):
        if B[i] == k:
            u += 1
    return u        

def findmax(B):
    max_val = B[0]
    max_index = 0
    for i in range(1, len(B)):
        if B[i] > max_val:
            max_val = B[i]
            max_index = i
    return max_val, max_index

def findmode(B):
    l1 = []
    sort_B = sort(B,"asc")
    l = find_distinct_elements(sort_B)
    a = len(l)
    for i in range(a):
        z = findfreq(sort_B,l[i])
        l1.append(z)
    maxv,maxi = findmax(l1) 
    return l[maxi]

def freqtable(B):
    z = find_distinct_elements(B)
    b = [findfreq(B,z[i]) for i in range(len(z))]
    c = [(z[i],b[i]) for i in range(len(z))]
    return c



         

