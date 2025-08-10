from lnm import A1

def swap(a, b, F):
    if F == "<":
        return (b, a) if a < b else (a, b)
    elif F == ">":
        return (b, a) if a > b else (a, b)
    else:
        raise ValueError("F must be '<' or '>'")

def checksort(B,order):
    a = len(B)
    for i in range(a-1):
        if order == "asc" and B[i] > B[i+1]:
            return False
        elif order == "desc" and B[i]<B[i+1]:
            return False
    return True    

def sort(A,order):
    if "asc" in order:
       flag = ">"
    elif "desc" in order:
       flag = "<"
    else:
       raise ValueError("Please type 'asc' for ascending or 'desc' for descending.")

    for j in range(len(A)):
        for i in range(len(A) - 1 - j):  # Optimize: skip sorted portion
            A[i],A[i + 1] = swap(A[i], A[i + 1], flag)  # Ascending order

    return A        

def main():
    order = input("ASCENDING or DESCENDING: ").lower()
    print("Sorted list:", sort(A1,order))
    return 0



if __name__ == "__main__":
    main()