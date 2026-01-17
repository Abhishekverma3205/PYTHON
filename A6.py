
#loop,while loop,for loop,nested loop
#indexing 

#create a list of 5 number.print the  frist element,last element and length of the list using indexing

numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Length of the list:", len(numbers))

#take a list of numbers and find the sum and average using built in functions

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)

#create a list of fruits ,add a new fruit using append and insert one at position 2

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.insert(2, 'grape')
print("Fruits list:", fruits)


#remove an element from the list using remove() and delete() the last element using pop()
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.remove('banana')
last_fruit = fruits.pop()
print("Fruits list after removal:", fruits)
print("Removed last fruit:", last_fruit)


#create a list with duplicate numbers use count() to check how many times a number is appear

numbers = [10, 20, 30, 20, 40, 20, 50]
count_20 = numbers.count(20)
print("Number 20 appears", count_20, "times in the list.")

#write a program to check if a number exist in the list or not 
numbers = [10, 20, 30, 40, 50]
num_to_check = 30
if num_to_check in numbers:
    print(num_to_check, "exists in the list.")
else:
    print(num_to_check, "does not exist in the list.")

#create a list of 5 integers use index to find the position of a given number
numbers = [10, 20, 30, 40, 50]
position = numbers.index(30)
print("Position of 30 in the list:", position)

#sort a list in accending and descending order using sort() and reverse=true
numbers = [50, 20, 40, 10, 30]
numbers.sort()
print("Sorted list in ascending order:", numbers)
numbers.sort(reverse=True)
print("Sorted list in descending order:", numbers)

#Reverse a list using reverse()
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print("Reversed list:", numbers)
