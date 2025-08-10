
def main():
    while 1:
        z = input("PASSWORD: ")
        if z != "HEY HI":
            print("WRONG PASSWORD\n TERMINATING PROGRAM!!!")
            break
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"A+B = {a+b}")

main()    