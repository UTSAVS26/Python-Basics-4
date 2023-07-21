def SwapAlternate(L):
     N = len(L)
     for i in range(0,N-1,2):
          L[i],L[i+1] = L[i+1],L[i]
A = [10,20,30,40,50,60,70]
print(A)
SwapAlternate(A)
print(A)
A = [12,34,56,65,43,23]
print(A)
SwapAlternate(A)
print(A)
