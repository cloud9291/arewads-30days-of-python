#1. Writ a function which generates a six digit/character random_user_id.

import random
import string

def generate_random_user_id():
    # Use digits and lowercase letters for the user ID
    characters = string.digits + string.ascii_lowercase
    
    # Generate a random six-character user ID
    random_user_id = ''.join(random.choice(characters) for _ in range(6))
    
    return random_user_id

random_id = generate_random_user_id()
print("Random User ID:", random_id)


#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random
import string

def user_id_gen_by_user():
    # Get user input for the number of characters
    num_characters = int(input("Enter the number of characters for each ID: "))

    # Get user input for the number of IDs to generate
    num_ids = int(input("Enter the number of IDs to generate: "))

    # Use digits and uppercase letters for the user ID
    characters = string.digits + string.ascii_uppercase

    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_characters))
        user_ids.append(user_id)

    return user_ids

generated_user_ids = user_id_gen_by_user()
print("Generated User IDs:", generated_user_ids)

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Format the RGB color string
    rgb_color = f"rgb({red},{green},{blue})"
    
    return rgb_color

print(rgb_color_gen())


#Exercises: Level 2
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(num_colors):
    hex_color = []

    for _ in range(num_colors):
        # Generate six random hexadecimal digits
        hex_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        
        # Format the hexadecimal color string
        hex_color.append('#' + hex_code)

    return hex_color

num_colors_to_generate = 5
result = list_of_hexa_colors(num_colors_to_generate)
print(result)

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(num_colors):
    colors = []
    
    for _ in range(num_colors):
        # Generate random RGB values in the range [0, 255]
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        
        # Append the RGB tuple to the list
        colors.append((red, green, blue))
    
    return colors

num_colors = 5
rgb_colors = list_of_rgb_colors(num_colors)
print(rgb_colors)


#3. Write a function generate_colors which can generate any number of hexa or rgb colors.

import random

def generate_colors(num_colors, color_format='hex'):
    colors = []

    for _ in range(num_colors):
        if color_format == 'hex':
            # Generate a random hexadecimal color code
            hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            colors.append(hex_color)
        elif color_format == 'rgb':
            # Generate random RGB values in the range [0, 255]
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            rgb_color = (red, green, blue)
            colors.append(rgb_color)
        else:
            raise ValueError("Invalid color format. Use 'hex' or 'rgb'.")

    return colors

# Generate a list of 5 random hexadecimal colors
num_colors = 5
hex_colors = generate_colors(num_colors, color_format='hex')
print(hex_colors)

#Generate a list of 5 random RGB colors
rgb_colors = generate_colors(num_colors, color_format='rgb')
print(rgb_colors)

# Exercises: Level 3
#1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(input_list):
    # Create a copy of the input list to avoid modifying the original list
    shuffled_list = input_list.copy()
    
    # Shuffle the copied list in place
    random.shuffle(shuffled_list)
    
    return shuffled_list

# Shuffle a list of numbers
original_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(original_list)
print("Original List:", original_list)
print("Shuffled List:", shuffled_list)

#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def generate_unique_numbers():
    # Generate a list of numbers from 0 to 9
    all_numbers = list(range(10))
    # Shuffle the list to get a random order
    random.shuffle(all_numbers)
    # Take the first seven numbers from the shuffled list
    unique_numbers = all_numbers[:7]
    
    return unique_numbers

random_numbers = generate_unique_numbers()
print('random nums are:', random_numbers)
