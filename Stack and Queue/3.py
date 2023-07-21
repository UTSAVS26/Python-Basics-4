# ===== STACK 3 =====
# ===== Country = [Country Name] =====

country = ["Paris", "England", "Mumbai", "Delhi", "London",
           "Washington", "Denmark", "Punjab", "Ottawa", "Rome"]
country_stack = []

def push():
    for name in country:
        if len(name) > 5:
            country_stack.append(name)
    print("\nCountry Name Pushed in Country Stack.")

def pop():
    if(country_stack == []):
        print("\nUnderflow / Country Stack is Empty.")
    else:
        country = country_stack.pop()
        print("\nPoped Element is:  ", country)
        
def traverse():
    if not (country_stack == []):
        print()
        n = len(country_stack)
        for i in range(n-1, -1, -1):
            print(country_stack[i])
    else:
        print("\nEmpty , No Country Stack to Display.")

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Traverse")
    print("4. Exit")
    ch=int(input("Enter Your Choice <1/2/3/4>: "))
    if(ch==1):
        push()
    elif(ch==2):
        pop()
    elif(ch==3):
        traverse()
    elif(ch==4):
        print("End")
        break
    else:
        print("Invalid Choice") 
