def Remove_characters(word, n):
    print(word)
    cut_word = word[n:]
    return cut_word

print(Remove_characters("AnyWord", 2))
print(Remove_characters("ReallyAnyWord", 4))
print(Remove_characters("ReallyReallyAnyWord", 10))