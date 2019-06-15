# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

string = input()
output_str = []

for key, group in groupby(string):
    output_str.append('(' + str(len(list(group))) + ', ' + str(key) + ')')

print(' '.join(output_str))
