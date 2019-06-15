# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())
words = OrderedDict()

for i in range(n):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(' '.join([str(num) for num in words.values()]))
