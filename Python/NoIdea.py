# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split(' ')
lst = input().split(' ')
A = input().split(' ')
B = input().split(' ')

table = {}
for item in A:
    table[item] = 1
for item in B:
    table[item] = -1

happiness = 0
for num in lst:
    happiness += table.get(num, 0)

print(happiness)
