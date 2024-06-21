# Convert the strings to lists of characters
str1 = list("cinema".lower())
str2 = list("iceman".lower())

# Bubble sort for str1
for i in range(len(str1)):
    for j in range(i+1, len(str1)):
        if str1[j - 1] > str1[j]:
            # Swap elements
            temp = str1[j]
            str1[j] = str1[j - 1]
            str1[j - 1] = temp

# Bubble sort for str2
for i in range(len(str2)):
    for j in range(i+1, len(str2)):
        if str2[j - 1] > str2[j]:
            # Swap elements
            temp = str2[j]
            str2[j] = str2[j - 1]
            str2[j - 1] = temp

# Compare sorted lists
if str1 == str2:
    print("The strings are anagrams")
else:
    print("They are not anagrams")

            

                