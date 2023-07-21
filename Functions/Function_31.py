def Disp(**Detail):
     print("Detail= ",Detail)
     for K,V in Detail.items():
          print(K,"->",V)
q = {"Name":10,"Score":[12,34]}
Disp(Q=q)
Disp(Q1="Priya",Q2=45,Q3=[23,56],Q4=34.5)
