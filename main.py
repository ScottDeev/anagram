# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    # Change the words to lower case and remove whitespaces
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')

    # Sort both input and then compare
    if(sorted(word1) == sorted(word2)):
        return True
    else:
        return False


print(find_anagrams('save', "vase"))
print(find_anagrams('a gentleman', "elegant man"))
