def minion_game(string):
    
    consonant_score = 0
    vowel_score = 0
    vowels = ["A", "E", "I", "O", "U"]
    
    # Do consonants and vowels at the same time.
    for i in range(len(string)):
        if string[i] in vowels:
            vowel_score += len(string) - i
        else:
            consonant_score += len(string) - i
    
    if consonant_score > vowel_score:
        print('Stuart ' + str(consonant_score))
    elif consonant_score < vowel_score:
        print('Kevin ' + str(vowel_score))
    else:
        print('Draw')

