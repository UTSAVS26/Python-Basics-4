G=10
def Test():
     L=G+20    # Local Var
     print("Local: ",L)
print("Main: ",G)
G+=30
Test()
print("Main: ",G)
