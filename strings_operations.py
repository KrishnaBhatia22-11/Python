# Accept input
text = input("Enter a string: ")

# Perform operations
upper_text = text.upper()
lower_text = text.lower()
reversed_text = text[::-1]
word_to_replace = input("Enter word to replace: ")
replacement_word = input("Enter replacement: ")
modified_text = text.replace(word_to_replace, replacement_word)

# Print results
print("Uppercase:", upper_text)
print("Lowercase:", lower_text)
print("Reversed:", reversed_text)
print("Modified String:", modified_text)
