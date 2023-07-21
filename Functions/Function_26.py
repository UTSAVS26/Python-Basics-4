def Sum(*N):
     S=0
     print("N= ",N)
     for i in N:
          S+=i
     return S
print(Sum(2))
print(Sum(5,8))
print(Sum(10,20,50,25))
