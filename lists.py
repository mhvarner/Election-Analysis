type(2019)
# Create a Python list to store your grocery list
shopping_list = ["milk","bread","eggs","peanut butter","jelly"]
# Print the grocery list
print(shopping_list)
# Change "Peanut Butter" to "Almond Butter" and print out the updated list
shopping_list[3] = "almond butter"
print(shopping_list)
# Remove "Jelly" from grocery list and print out the updated list
shopping_list.remove("jelly")
print(shopping_list)
# Add "Coffee" to grocery list and print the updated list
shopping_list.append("coffee")
print(shopping_list)
#-------------------------------------------------------------------------------
# ToDo: Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
print("\n\n")

nums = range(11)
for num in nums:
    print(num)
