def TenSum(*N):
     S = 0
     for i in N:
          if i%10 == 0:
               S +=i
     return S
print(TenSum(20,34,19))
print(TenSum(5,80,3))
print(TenSum(10,24,50,20))
