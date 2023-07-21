def RaiseMarks(S,P):
     S["Marks"] *= ((100+P)/100)
     S["Status"] = "Changed"
S1 = {"Rno":1,"Name":"Raj","Marks":75,"Status":"*"}
S2 = {"Rno":3,"Name":"Ken","Marks":60,"Status":"*"}
RaiseMarks(S1,5)
RaiseMarks(S2,10)
print(S1)
print(S2)
