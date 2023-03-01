from cw1 import Queue

n = int(input())
q = Queue()

q.append("1")

for i in range(n):
    a = q.pop_front()
    new_a1 = a + "0"
    new_a2 = a + "1"
    q.append(new_a1)
    q.append(new_a2)
    print(a, end=" ")