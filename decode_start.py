alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f:
        nr_vowels = 0
        for v in vowel:
           nr_vowels += line.count(v) #count the amt of time that particular vowel should show up
        letter = alphabet[nr_vowels]
        message += letter
print(message)