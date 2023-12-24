#1. What is the most frequent word in the following paragraph?
word_counts = [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
]

# Find the word with the maximum count
most_frequent_word = max(word_counts, key=lambda x: x[0])[1]

print("The most frequent word is:", most_frequent_word)


#2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
sorted_points = [-12, -4, -3, -1, 0, 4, 8]

# Find the distance between the two particles
distance = sorted_points[-1] - sorted_points[0]

print("Distance between the two furthest particles:", distance)


# Exercises: Level 2
#1. Write a pattern which identifies if a string is a valid python variable

import re

def is_valid_variable(variable_name):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(pattern.match(variable_name))
# Test cases
print(is_valid_variable("valid_variable"))  # True
print(is_valid_variable("_underscore"))      # True
print(is_valid_variable("123_invalid"))      # False
print(is_valid_variable("no spaces"))         # False

#.Exercises: Level 3
#1. Clean the following text. After cleaning, count three most frequent words in the string.

import re
from collections import Counter

def clean_text(text):
    # Remove special characters and extra spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def most_frequent_words(text, num_words=3):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(num_words)

# Given sentence
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean the text
cleaned_text = clean_text(sentence)
print(cleaned_text)

# Find the three most frequent words
result = most_frequent_words(cleaned_text)
print(result)

