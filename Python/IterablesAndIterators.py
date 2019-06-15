# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

N = int(input())
letters = input().split(' ')
K = int(input())
perms = permutations(letters, K)
count = 0
total = 0

for p in perms:
    total += 1
    if 'a' in p:
        count += 1

print(round(count / total, 3))
