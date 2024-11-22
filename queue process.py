import collections

pl = input("words separated: ")
words = pl.split()
queue= collections.deque()

for i in words:
    queue.appendleft(i)
print("Initial Queue: ", queue)

print("words with 'o': ")

for word in queue:
    if 'o' in word:
        print(word)