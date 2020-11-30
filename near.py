def near(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    test = word1.copy()
    for i in range(len(word1)):
        test.pop(i)
        if test == word2:
            return True
        test = word1.copy()
    
    return False





print(near("reset","rest"))