i=[90,100]
def test():
     global i
     i[0]+=10
     i[1]+=20
     print(i)
test()
print(i)
