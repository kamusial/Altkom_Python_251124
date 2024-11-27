from collections import deque

deq = deque([1, 2, 3, 4, 5])
deq.append(6)
deq.appendleft(0)   # dodaj na początek
print(deq)
deq.pop()
deq.popleft()  # usuń z poczatku
print(deq)