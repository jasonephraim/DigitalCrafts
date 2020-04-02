def palindrome(word = str.lower(input("Please enter a word: "))):
    word2 =''.join(reversed(word))
    if word == word2:
        print(word, "is a palindrome!")
    else:
        print(word, "is not a palindrome")
palindrome()