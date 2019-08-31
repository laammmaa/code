S = "please, I want {} sandwishes and {} donutes"
# Replacing "I" to "We" using replace()
# Adding 5 and 7 to the sentence using format()
# Replacing any "a" to "A" using replace()
new_s = S.format(5, 7).replace("I", "We").replace("a", "A", len(S))
print(new_s)
