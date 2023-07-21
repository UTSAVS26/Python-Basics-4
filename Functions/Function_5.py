def Scholars(L):
     S=[]
     for i in L:
          if i>90:
               S.append(i)
     return S
L1 = [67,98,45,92]
L2 = [95,58,95,99,87]
SLR1 = Scholars(L1)
SLR2 = Scholars(L2)
print("L1: ",L1)
print("Scholar Marks: ",SLR1)
print("L2: ",L2)
print("Scholar Marks: ",SLR2)
