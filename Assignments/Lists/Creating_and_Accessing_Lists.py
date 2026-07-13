# # Module 3: Data Structures Assignments
# ## Lesson 3.1: Lists
# ### Assignment 1: Creating and Accessing Lists


# Create a list of the first 20 positive integers. Print the list.
numbers_20=list(range(1, 21))
print(numbers_20)
# ### Assignment 2: Accessing List Elements

# Print the first, middle, and last elements of the list created in Assignment 1.
first,middle,last=numbers_20[0],numbers_20[len(numbers_20)//2],numbers_20[-1]
print(f"First element: {first}, Middle element: {middle}, Last element: {   last}")
# ### Assignment 3: List Slicing

# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
first_five=numbers_20[0:5]
last_five=numbers_20[-5:]
elements_5_to_15=numbers_20[5:16]
print(f"First five elements: {first_five}")
print(f"Last five elements: {last_five}")
print(f"Elements from index 5 to 15: {elements_5_to_15}")
# ### Assignment 4: List Comprehensions

# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
first_10_positive=[i**2 for i in range(1,11)]
print(f"Squares of the first 10 positive integers: {first_10_positive}")
# ### Assignment 5: Filtering Lists

# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
even_list=[i for i in numbers_20 if i%2==0]
print(f"Even numbers from the list: {even_list}")