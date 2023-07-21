import sys

book = []
print("1. Add a Book Detail")
print("2. Delete a Book Detail")
print("3. Display all Records")
print("4. Exit")

option = int(input("Enter Your Choice: "))
while option != 4:
    if option == 1:
        book_name = input("Enter Book Name: ")
        book_no = int(input("Enter Book No.: "))
        detail = [book_name, book_no]
        book.append(detail)
        print(book, "\n")
    if option == 2:
        book.pop()
        print(book, "\n")
    if option == 3:
        for i in book:
            print(i)
    if option == 4:
        sys.exit()
    option = int(input("Enter Your Choice: "))
