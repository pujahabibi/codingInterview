#Given two strings, check if they are anagrams. An anagram is when the two strings can be written
# using the exact same letters (so you can just rearrange the letters to get a different phrase or word)

#for example:
#"public relations" is anagram of "crap built on lies"

def anagram(s1, s2):
    s1 = s1.replace(" ", '').lower()
    s2 = s2.replace(" ", '').lower()
    return sorted(s1) == sorted(s2)

print(anagram("Public Relations", "crap built on lies"))
stringTyped = "crap built on lies"
sws = stringTyped.replace(" ", "").lower()
print(sorted(sws))