# BUILTINS
# print()    input()    len()    type()    id()

#GLOBAL
id=25

#ENCLOSING
def First():
     id=35
     print(id)

     #LOCAL
     def Second():
          id=45
          print(id)

     Second()

First()
print(id)
