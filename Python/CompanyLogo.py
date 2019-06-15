if __name__ == '__main__':
    
    companyName = input()
    
    # Make table of letter occurrences.
    char_counts = {}
    for char in companyName:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    ordered_chars = sorted(char_counts.keys())
    ordered_chars = list(sorted(ordered_chars, key=lambda x:char_counts[x], reverse=True))

    for char in ordered_chars[:3]:
        print(char + ' ' + str(char_counts[char]))
