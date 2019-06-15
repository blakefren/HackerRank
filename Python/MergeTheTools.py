def merge_the_tools(string, k):
    
    # Process each subsegment.
    for i in range(len(string)//k):
        letters = {}
        subsegment = string[k*i:k*(i+1)]
        final_sub = []
        for letter in subsegment:
            if letter in letters:
                continue
            else:
                final_sub.append(letter)
                letters[letter] = True
        print(''.join(final_sub))


