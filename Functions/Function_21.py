G = {"Tap":75,"Ram":82}
def Raise(R):
     G["Tap"] += R
     G["Ram"] += R
     print("After Raise: ",G)
print("Main: ",G)
r = 10
Raise(r)
print("Main: ",G)
