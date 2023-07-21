G = 10
def Test1():
     G = 20
     print("Test1 G: ",G)
def Test2():
     G = 30
     print("Test2 G: ",G)
print("Main G: ",G)
G += 5
Test1()
print("Main G: ",G)
G += 10
Test2()
print("Main G: ",G)
