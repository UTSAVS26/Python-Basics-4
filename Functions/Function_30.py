def GetPoints(p,**E):
     print("E= ",E)
     if (type(E.get("Level")) == int and
              E["Level"]%5 == 0):
          p += 10
          print("Awarded: ",p,"Points")
     if E["Bonus"] == "Yes":
          p *= 2
          print("Awarded: ",p,"Points")
     return p
P = 0
P = GetPoints(P,Level=2,Bonus="Yes")
P = GetPoints(P,Level=5,Bonus="No")
P = GetPoints(P,Level=10,Bonus="Yes")
P = GetPoints(P,Bonus="Yes")
