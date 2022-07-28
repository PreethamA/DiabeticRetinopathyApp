#Write a routine that takes in two strings and checks if the two strings are anagrams of each other.
# An anagram is a word, phrase, or name formed by rearranging the letters of another
'''
str1 = "spar"
str2 = "rasp"
s1 = "arc"
s2 = "car"
'''
def ana(str1, str2):

    if len(str1) != len(str2):
        return -1

    d1 = {}
    d2 = {}


    for i in range(len(str1)):
        if str1[i] not in d1.keys():
            d1[str1[i]] = 1
        else:
            d1[str1[i]] += 1

        if str2[i] not in d2.keys():
            d2[str2[i]] = 1
        else:
            d2[str2[i]] += 1

    return "Anagram" if d1 == d2 else "Not Anagram"

if __name__ == "__main__":
    # run the application
    str1 = "racc"
    str2 = "arcc"
    print(ana(str1, str2))