from collections import deque

numbers = input("numbers separated: ")
stack = deque(numbers.split())

print("stack1", stack)

for i in range(len(stack)):
    number = stack.pop()
    print(int(number)** 2)

