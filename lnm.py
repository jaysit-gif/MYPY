import random 
A = [random.randint(1,100) for _ in range(1,100)]
z = random.randint(100,200)
a = random.randint(1,50)
A2 = [random.randint(a,z) for _ in range(a,z)]
A1 = [random.randint(z-a,z+a) for _ in range(a,z+a)]

