word = "RemoveOddIndexedCharactersFromThisWord"
isEven = True

for x in word:
    if isEven:
        print(x, end ="")
        isEven = False
    else:
        isEven = True
print("\n")


    