
# INCOMPLETE
# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdin


q = int(stdin.readline())
input_lst = []

for i in range(q):
    input_lst.append(stdin.readline().rstrip().split(' '))
    
    r = 1
    a = int(input_lst[0][0])
    d = int(input_lst[0][1])
    n = int(input_lst[0][2])
    x = int(input_lst[0][3])

    rounded_r = 1
    change = 0.1
    s_n = 0
    num_decimals = 0
    while num_decimals <= 12 and abs(s_n - (-x)) > 0.1:
    # while abs(s_n - (-x)) > 0.1:
        s_n = sum([((a - d * k) * r**(k-1)) for k in range(1, n+1)])
        
        if s_n > (-x):
            r += change
        else:
            r -= change
        
        change /= 2
        rounded_r = round(r, len(str(int(r)))+11)
        if "." in str(rounded_r):
            num_decimals = len(str(rounded_r)) - str(rounded_r).index(".") - 1
        print(rounded_r, num_decimals, num_decimals < 12)

    print(round(r, len(str(int(r)))+11))
