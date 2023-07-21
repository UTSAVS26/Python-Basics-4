def HalfSwap(L):
     n = len(L)
     for i in range(n//2):
          L[i],L[n//2+i] = L[n//2+i],L[i]
A = [10,20,30,40,50,60,70]
print(A)
HalfSwap(A)
print(A)
A = [12,34,56,65,43,23]
print(A)
HalfSwap(A)
print(A)
