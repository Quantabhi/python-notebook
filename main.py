# Python note book  

# 1. len() function
test = 'aaaaaaaa'
print(len(test))  # Output: 8

# 2. input() function
age = input('What is your age: ')
print(age)

# 3. type() function
test = 123
print(type(test))  # Output: <class 'int'>

# 4. range() function with for loop
for i in range(5):
    print(i)

# 5. map() function with str.capitalize
name = ['abhi', 'riya', 'rahul']
capitalized_names = map(str.capitalize, name)
print(list(capitalized_names))

# 6. max() and min() functions
num = [1, 2, 3, 2, 4, 55, 66, 7, 222, 8]
print('The max:', max(num), 'and the min:', min(num))

# 7. Tuples in Python
fruits = ('orange', 'apple', 'pear', 'banana', 26, 11)
print(fruits)
print(type(fruits))  # Output: <class 'tuple'>

# 8. Python Class and Object Example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects
a1 = Student('rahul', 21)
a2 = Student('disha', 20)

# Printing object attributes
print(a1.name, a2.name)
print(a1.age, a2.age)

# 9. Lists in Python
lis = ['abc', 'xxdy', 123]
print(lis)
print(type(lis))  # Output: <class 'list'>

# 10. While Loop
count = 1
while count <= 5:
    print(count)
    count += 1
print("Loop finished!")

# 11. Using lambda with filter() to filter a list (even numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# 12. Dictonaries 
test_dic = {'abhi':26,'city':'gola'}
print(test_dic)
print(type(test_dic))

#13. if else 
age = int(input('what is your age: '))
if age > 18:
    print('you can vote')
else:
    print('you are not eligible for vote')    

