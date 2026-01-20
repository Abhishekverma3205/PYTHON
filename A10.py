
#Functions 

#write a program that prints hello world
def hello_world():
    print("Hello, World!")
hello_world()

#write a function that takes a names as input and prints "Hello, <name>!"
def greet(name):
    print(f"Hello, {name}!")
greet("vasu")

#write a function that takes two numbers as input and print their sum 

def add_numbers(a, b):
    return a + b
result = add_numbers(10, 10)
print("sum =", result)

#write a function that returns the square of a nummber 

def square(n):
    return n * n
print("Square of 20 is ", square(20))

#write a function to check number is odd or even
def check_odd_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_odd_even(19))

#write a function that takes two numbers and returns theier maximum
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print("Maximum is ", maximum(10, 20))

#write a function that takes a list of numbers and returns their average

def average(numbers):
    return sum(numbers) / len(numbers)
print("Average is ", average([10, 20, 30, 40, 50]))

#write a function that counts vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print("Number of vowels =", count_vowels("Hello World"))


#write a recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is ", factorial(5))

#write a function to check if a string is palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print("Is 'madam' a palindrome? ", is_palindrome("madam"))


#write a function that calculates simple interest(default rate = 5%)
def simple_interest(principal, time, rate=5):
    return (principal * rate * time) / 100
print("Simple Interest is ", simple_interest(1000, 2))

#write a function that takes a name and age and prints them(use keyword arguments)
def print_name_age(name, age):
    print(f"Name: {name}, Age: {age}")
print_name_age(name="Vasu", age=20)

#write a recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 6 is ", factorial(6))

#write a recursive function to print fibonacci upto n terms
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
print("Fibonacci sequence upto 10 terms: ", fibonacci(10))

#write a function that takes a list of numbers and returns the largest elements
def largest_element(numbers):
    return max(numbers)
print("Largest element is ", largest_element([10, 20, 5, 40, 30]))

#write a function that takes a dictionary and print all key value pairs
def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")
sample_dict = {"a": 1, "b": 2, "c": 3}
print_dict(sample_dict)

#Write a function that takes a set and returns its length. 
def set_length(s):
    return len(s)
print("Length of set is ", set_length({1, 2, 3, 4, 5}))

#Write a function that takes a list of dictionaries (students with marks) and returns the topper’s name. 
def find_topper(students):
    topper = max(students, key=lambda x: x['marks'])
    return topper['name']
students_list = [
    {"name": "Vaibhav", "marks": 85},
    {"name": "Shakti", "marks": 9},
    {"name": "Falak", "marks": 78}
]
print("Topper is ", find_topper(students_list))
