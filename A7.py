
#tupples, sets 


#create a set of 5 colors and print it
colors = {"red", "blue", "green", "yellow", "purple"}
print(colors)

#create a set of numbers with duplicates and check how python handles duplicates
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)  

#write a program to loop through the set and print each element
for color in colors:
    print(color)

#Create a set and use add() to insert a new element
colors.add("orange")
print(colors)

#remove an element using remove() and oberve what happens if the element is not present
colors.remove("blue")
print(colors)

#remove an element using discard() and compare it with remove() 
colors.discard("pink")  
print(colors)

#use pop() to remove a random element from the set
removed_color = colors.pop()
print("Removed color:", removed_color)
print(colors)

#create two sets and find their union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

#create two sets and find their intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

#create two sets and find the difference(A-B)
difference_set = set1.difference(set2)
print("Difference (A-B):", difference_set)

#use copy() to create a copy of a set and modify the copy
set_copy = colors.copy()
set_copy.add("cyan")
print("Original set:", colors)
print("Modified copy:", set_copy)


#use clear to empty a set
set_copy.clear()
print("Cleared set:", set_copy)
print("Original set after clearing copy:", colors)


#convert a list with duplicates into a set to remove duplicates
my_list = [1, 2, 3, 4, 5, 6]
my_set = set(my_list)
print("set from list:", my_set)
print("Original list:", my_list)


#write a program to find all unique characters in a string using sets
my_string = "hello world"
unique_chars = set(my_string)
print("Unique characters:", unique_chars)

#given two list of students(cricket and football), find students who play both sports(intersection)

cricket_players = {"Alice", "Bob", "Charlie", "David"}
football_players = {"Charlie", "David", "Eve", "Frank"}
both_sports = cricket_players.intersection(football_players)
print("Students who play both sports:", both_sports)


#given two list of students,find students who play only cricket(difference)

only_cricket = cricket_players.difference(football_players)
print("Students who play only cricket:", only_cricket)


#take a sentence as input and print all unique words using sets
sentence = "this is a test this is only a test"
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Sum of digits =")


#write a program to check if two sets are equal(ignorinng order)
set1 = {1, 2, 3}
set2 = {3, 2, 1}
print("Are sets equal?", set1 == set2)

#create two sets and check if they at least one common element(hint: use intersaction)
setA = {1, 2, 3}
setB = {4, 5, 3}
common_elements = setA.intersection(setB)
print("Do sets have common elements?", len(common_elements) > 0)
