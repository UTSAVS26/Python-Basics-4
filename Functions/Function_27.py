def TenSum(*N):
     S = 0
     for i in N:
          if type(i) is int or type(i)is float:
                    if i%10 == 0:
                         S +=i
          else:
               print("Unsupported Type")
     return S
print(TenSum(20,34,19))
print(TenSum(5,"A",30))
print(TenSum("Big",24,50,20))
