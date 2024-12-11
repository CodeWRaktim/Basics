# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

# # def multiple_values(x, y):
# #     sum = x + y
# #     product = x * y
# #     return sum, product
# # result = multiple_values(5, 3)
# # sum_value, product_value = result

# # print("Sum:", sum_value)
# # print("Product:", product_value)
# # def power(base, exponent=2):

# #     return base ** exponent
# # print(power(3))       # Output: 9 (3^2)
# # print(power(2, 3))    # Output: 8 (2^3)
# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)

# # # Example usage:
# # print("The factorial is:",factorial(5))  # Output: 120
# # print("The factorial is:",factorial(3))  # Output: 6
# # def greet(name):
# #     """
# #     This function greets the person passed in as a parameter
# #     """
# #     print(f"Hello, {name}!")

# # # Assign a different name to the function
# # say_hello = greet

# # # Call the function using the new name
# # say_hello("Alice")  # Output: Hello, Alice!
# # say_hello("Bob")    # Output: Hello, Bob!

# # def count_upper_lower(string):
# #     upper_count = 0
# #     lower_count = 0

# #     for char in string:
# #         if char.isupper():
# #             upper_count += 1
# #         elif char.islower():
# #             lower_count += 1

# #     return upper_count, lower_count
# # string = "The quick Brown Fox"
# # upper, lower = count_upper_lower(string)
# # print("No. of Upper case characters :", upper)
# # print("No. of Lower case Characters :", lower)
# def sort_hyphenated_sequence(sequence):
#     words = sequence.split('-')
#     words.sort()
#     return '-'.join(words)

# # Example usage:
# # input_sequence = "green-red-yellow-black-white"
# # sorted_sequence = sort_hyphenated_sequence(input_sequence)
# # print(sorted_sequence)  # Output: black-green-red-white-yellow
# # import sys

# # def sys_info():
  
# #   print("Python version:", sys.version)
# #   print("Command-line arguments:", sys.argv)

# # if __name__ == "__main__":
# #   sys_info()

# import time

# def display_time_info():
#     # Get the current time in seconds since the Epoch
#     current_time = time.time()
#     print("Current time (seconds since Epoch):", current_time)
    
#     # Convert the current time to a readable format
#     local_time = time.localtime(current_time)
#     print("Local time:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))
    
#     # Get the current time in UTC
#     # utc_time = time.gmtime(current_time)
#     # print("UTC time:", time.strftime("%Y-%m-%d %H:%M:%S", utc_time))
    
#     # Measure the time taken by a small code snippet
#     start_time = time.time()
#     for i in range(1000000):
#         pass
#     end_time = time.time()
#     print("Time taken to execute loop:", end_time - start_time, "seconds")
    
#     # Pause the program for a specified number of seconds
#     print("Pausing for 2 seconds...")
#     time.sleep(2)
#     print("Resumed after pause")

# if __name__ == "__main__":
#     display_time_info()

# import os

# def display_os_info():
#     # Get the current working directory
#     cwd = os.getcwd()
#     print("Current working directory:", cwd)
    
#     # List files and directories in the current directory
#     files_and_dirs = os.listdir(cwd)
#     print("Files and directories in '", cwd, "':", files_and_dirs)
    
#     # Create a new directory
#     new_dir = "test_dir"
#     if not os.path.exists(new_dir):
#         os.mkdir(new_dir)
#         print("Directory '", new_dir, "' created")
#     else:
#         print("Directory '", new_dir, "' already exists")
    
#     # Rename the directory
#     renamed_dir = "renamed_test_dir"
#     if os.path.exists(new_dir):
#         os.rename(new_dir, renamed_dir)
#         print("Directory '", new_dir, "' renamed to '", renamed_dir, "'")
    
#     # Remove the directory
#     if os.path.exists(renamed_dir):
#         os.rmdir(renamed_dir)
#         print("Directory '", renamed_dir, "' removed")
    
#     # Get the current process ID
#     pid = os.getpid()
#     print("Current process ID:", pid)
    
#     # Get the list of environment variables
#     env_vars = os.environ
#     print("Environment variables:", env_vars)

# if __name__ == "__main__":
#     display_os_info()

import random

def display_random_info():
    # Generate a random float number between 0 and 1
    random_float = random.random()
    print("Random float between 0 and 1:", random_float)
    
    # Generate a random integer between 1 and 10
    random_int = random.randint(1, 10)
    print("Random integer between 1 and 10:", random_int)
    
    # Choose a random element from a list
    sample_list = ['apple', 'banana', 'cherry', 'date']
    random_choice = random.choice(sample_list)
    print("Random choice from list:", random_choice)
    
    # Shuffle a list
    random.shuffle(sample_list)
    print("Shuffled list:", sample_list)
    
    # Generate a random sample of 2 elements from a list
    random_sample = random.sample(sample_list, 2)
    print("Random sample of 2 elements from list:", random_sample)
    
    # Generate a random float number between 1 and 10
    random_uniform = random.uniform(1, 10)
    print("Random float between 1 and 10:", random_uniform)

if __name__ == "__main__":
    display_random_info()
