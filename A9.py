#Dictionary methods

#create a dictionary of students and marks. Use. keys(), to print all the student names.
students_marks ={
    "Vaibhav": 85,
    "Shakti": 92,
    "Falak": 78,
    "Sagar": 95,
    "Awani": 88,
    "Rudransh": 90
}
print(students_marks.keys())


#use values() to print all the marks
print(students_marks.values())

#use items() to print all the key value pairs
print(students_marks.items())

#use get() method to access the marks of "Sagar"(if not found return "Not Found")
print(students_marks.get("Sagar", "Not Found"))


#use update() method to update the marks of "Falak" to 80

students_marks.update({"Falak": 80})
print(students_marks)

#Removing Elements

#use pop(Key) to remove "shakti" from the dictionary
students_marks.pop("Shakti")
print(students_marks)

#try popping a non existing key using pop() with a default value
removed_value = students_marks.pop("Ankit", "Key Not Found")
print(removed_value)

#use .clear() method to remove all elements from the dictionary
students_marks.clear()
print(students_marks)
