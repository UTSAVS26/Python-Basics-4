# ===== STACK 2 =====
# ===== World = {Country : Continent} =====
# ===== World_Stack = [Country] =====

world = {"UK" : "EUROPE", "INDIA" : "ASIA", "CHINA" : "ASIA",
         "EGYPT" : "AFRICA", "CUBA" : "AMERICA", "JAPAN" : "ASIA"}
world_stack = []

def push():
    for continent in world:
        if world[continent] == "ASIA":
            world_stack.append(continent)
    print("\nCountry Name Pushed in World Stack.")

def pop():
    if(world_stack == []):
        print("\nUnderflow / World Stack is Empty.")
    else:
        country = world_stack.pop()
        print("\nPoped Element is:  ", country)
        
def display():
    if not (world_stack == []):
        print()
        n = len(world_stack)
        for i in range(n-1, -1, -1):
            print(world_stack[i])
    else:
        print("\nEmpty , No World Stack to Display.")

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    ch=int(input("Enter Your Choice <1/2/3/4>: "))
    if(ch==1):
        push()
    elif(ch==2):
        pop()
    elif(ch==3):
        display()
    elif(ch==4):
        print("End")
        break
    else:
        print("Invalid Choice") 
