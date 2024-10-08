def vowelsToUpper(string):
# List comprehension: Convert vowels to uppercase, leave other characters unchanged
    return ''.join([char.upper() if char in 'aeiouAEIOU' else char for char in string])

# Sample strings
sample_string = "What a wonderful day, so good, so amazing, huwaw!"

# Print the result
print("Vowels to uppercase:", vowelsToUpper(sample_string))