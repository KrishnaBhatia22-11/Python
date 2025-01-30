string = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("\nVowel Count:", vowel_count)
print("Consonant Count:", consonant_count)
print("Krishna Bhatia 1/23/SET/BCS/358")
