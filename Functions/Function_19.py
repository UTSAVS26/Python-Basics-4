G = 100
def Function1():
     global G
     G += 20
     print(G)
print(G)
G += 10
print(G)
Function1()
print(G)
