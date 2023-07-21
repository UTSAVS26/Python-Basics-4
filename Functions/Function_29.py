def Multi(**P):
     print(type(P))
     print(P)
     for k,v in P.items():
          print(k,"->",v)
Multi(Name="Suraj",Fee=3000,Type="Guest")
s = {"Ino":11,"Item":"Pen","Qty":40}
Multi(Stock=s)
