G = [100,200]
def Raise(R):
     G[0] += R
     G[1] += R
     print("After Raise: ",G)
print("Main: ",G)
r =10
Raise(r)
print("Main: ",G)
