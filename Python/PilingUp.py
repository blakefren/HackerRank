# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

t = int(input())
answers = []

for i in range(t):
    
    n = int(input())
    ints = deque([int(item) for item in list(input().split(' '))])
    top_size = 2**31
    
    # Pop either the left or right block.
    while ints:
        
        # Left
        if ints[0] >= ints[len(ints)-1] and ints[0] <= top_size:
            top_size = ints.popleft()
        
        # Right
        elif ints[0] <= ints[len(ints)-1] and ints[len(ints)-1] <= top_size:
            top_size = ints.pop()
        
        # No solution
        else:
            answers.append('No')
            break
    
    # If no more ints, then successful.
    if len(ints) == 0:
        answers.append('Yes')
        
        
        
for s in answers:
    print(s)
