from lnm import A1
from test import linear_search, binary_search, findfreq, findmode, findmean,findmax,find_distinct_elements,freqtable


def fintput():
    y = input("S: ").lower()    
    if y != "summary":
        x = int(input("ENTER NUMBER: "))         
    else :
        x = 0
    return x,y

def fout(x,y,z):
    print(f"through {y},{x} was found on {z}")

def main():  
    x,y = fintput()
    if y == "binary search":
        z,sort_A = binary_search(A1,x)
        fout(x,y,z) if z != -1 else print(f"SORRY!! {x},NOT FOUND") 
        print("SORTED LIST: ",sort_A)
    elif y == "linear search":
        z = linear_search(A1,x)
        fout(x,y,z) if z != -1 else print(f"SORRY!! {x},NOT FOUND")   
    elif y == "find frequency":
        z = findfreq(A1,x)     
        print(f"the number {x} has frequency of {z}")
    elif y == "mode":
        z = findmode(A1,x)
        print(f"MODE: {z}")  
    elif y == "summary":
      print(f"Mean: {findmean(A1)}")
      print(f"Mode: {findmode(A1)}")
      print(f"Max: {findmax(A1)}")
      print(f"Distinct: {find_distinct_elements(A1)}")
      print(f"FREQUENCY TABLE: {freqtable(A1)}")
    else:
        print("COMMAND INVALID")  
        i = ["binary search", "linear search", "find frequency", "mode", "summary"]
        print(f"valid commands: {i}")      

    return 0

main()
