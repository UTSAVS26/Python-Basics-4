# ===== STACK 1 =====
# ===== Book Details : [Book Code, Book Title, Book Price] =====

book = []

def push():
    bcode = int(input("\nEnter Book Code:  "))
    btitle = input("Enter Book Title: ")
    price = float(input("Enter Book Price: "))
    bk = [bcode,btitle,price]
    book.append(bk)

def pop():
    if(book == []):
        print("\nUnderflow / Book Stack is Empty.")
    else:
        bcode, btitle, price = book.pop()
        print("\nPoped Element is:  ")
        print("\tBook Code\tBook Title\t\tBook Price")
        print("\t", bcode, "\t\t", btitle, "\t\t", price)
        
def traverse():
    if not (book == []):
        print()
        n = len(book)
        for i in range(n-1, -1, -1):
            print(book[i])
    else:
        print("\nEmpty , No Book to Display.")

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Traversal")
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
