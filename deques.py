from collections import deque

deq = deque((1,4,5,3,2))

print(deq.popleft())
print(deq.pop())
print(deq.pop())
print(deq.popleft())
print(deq.count(5)*5)
