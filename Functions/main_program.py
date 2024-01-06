# main_program.py

# Approach 1: import module_name
import helper_functions

helper_functions.my_function()

# Approach 2: from module_name import function_name
from helper_functions import my_function

my_function()

# Approach 3: from module_name import function_name as fn
from helper_functions import my_function as fn

fn()

# Approach 4: import module_name as mn
import helper_functions as mn

mn.my_function()

# Approach 5: from module_name import *
from helper_functions import *

my_function()
