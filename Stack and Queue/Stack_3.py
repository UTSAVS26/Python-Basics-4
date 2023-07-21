dict_stack = {}
list_stack = []

choice = int(input("Enter No. of Records: "))
for i in range(choice):
    name = input("\n Enter Name of Student No. %s: "%(i+1))
    marks = float(input(" Enter Marks: "))
    dict_stack[name] = marks

print("\n\t STACK ITEMS")
for i in dict_stack:
    if dict_stack[i] > float(75):
        item = [i, dict_stack[i]]
        list_stack.append(item)
        print(item)
print("\n The List Contains following Records: ")
print(list_stack)

def pop(list_stack):
    if list_stack != []:
        pop_element = list_stack.pop()
        print("POP Element: ", pop_element)
        print("\nFINAL Stack: ", list_stack)
    else:
        print("Empty Stack")

# ===== MAIN PROGRAM =====
while True:
    ch = input("\n\t Do You Want to Pop Item (Y/N): ")
    if ch.lower() == "y":
        pop(list_stack)
    else:
        break
