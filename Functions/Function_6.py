def Scholars(ST):
     S = {}
     for k,v in ST.items():
          if v>=90:
               S[k] = v
     return S
S1 = {"Anu":67,"Raj":98,"Ken":45,"Ram":92}
SR1 = Scholars(S1)
print(S1)
print(SR1)
