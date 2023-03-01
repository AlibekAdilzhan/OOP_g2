from cw1 import Queue


q = Queue()

run = True
text_1 = """0. Exit
1. Add element
2. Delete element
3. Get size
4. Get peek
5. Show queue
"""

while run:
    choice = int(input(text_1))
    if choice == 1:
        x = input("Please, enter the element: ")
        q.append(x)
    elif choice == 2:
        q.pop_front()
    elif choice == 4:
        print(q.peek())
    elif choice == 3:
        print(q.size())
    elif choice == 5:
        print(q)
    elif choice == 0:
        run = False
    