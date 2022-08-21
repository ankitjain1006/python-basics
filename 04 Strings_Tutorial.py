phrase = "Ankit"
phrase = phrase + " Kumar"
phrase = phrase + " Jain"

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

print(len(phrase))

# Index on string is start from 0
print(phrase[0])
print(phrase[6])


print(phrase.index("A"))
print(phrase.index("K"))

print(phrase.replace(" Kumar", ""))