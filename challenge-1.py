
# Challenge 1

n = int(input("Enter number:"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum, "<---- Challenge 1")

# Challenge 2

def largest(list1):
    max = list1[0]
    for x in list1:
        if x > max :
             max = x 
    return max
  
list1 = [10, 20, 4, 45, 99, 120]
print("Largest element is:", largest(list1), "<---- Challenge 2")

# Challenge 3

print("flee fleeing flead".count("e"), "<---- Challenge 3")


# Challenge 4

def multiply(*args):
    product = 1
    for item in args:
        product *= item
    return product

print(multiply(1), "<---- Challenge 4")
print(multiply(1,2), "<---- Challenge 4")
print(multiply(1,2,3), "<---- Challenge 4")

from itertools import count


# nums = [1, 3, 2, 6, 5]
# odds = list( filter(lambda num: num % 2, nums) )
# print(odds)

# def add(a, b):
#   return a + b
  
# def sub(a, b):
#   return a - b

# def compute(a, b, op):
#   return op(a, b)

# print( compute(1, 2, add) )

# def dev_skills(dev_name, *args):
#   dev = {'name': dev_name, 'skills': []}
#   for skill in args:
#     dev['skills'].append(skill)
#   return dev

# print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))

# def dev_skills(dev_name, **kwargs):
#   dev = {'name': dev_name, 'skills': {}}
#   # unpacking the tuples returned by the items function
#   for skill, rating in kwargs.items():
#     dev['skills'][skill] = rating
#   return dev

# print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))












