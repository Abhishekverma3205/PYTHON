
# Dictionaries and Nested Data Structures

student = {
    "name": "Vaibhav",
    "age": 20,
    "address": "Lucknow",
}
print(student["name"])  

print(student.get("address"))

print(student.get("phone", "Not Available"))
student["phone"] = "123-456-7890"
print(student)

print(student.keys())


#crerate a dictionary of 5 countries and their capitals. print it.
countries_capitals = {
    "India": "New Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Brazil": "Brasília"
}
print(countries_capitals)


#access the capital of "india"

print(countries_capitals["India"])

#add a new key value pair "china"  : "beijing" in the dictionary
countries_capitals["china"] = "Beijing"
print(countries_capitals)

#update the capital of "germany" to "Munich"
countries_capitals["Germany"] = "New York"
print(countries_capitals)

#delete the key value pair of "brazil" using del keyword
del countries_capitals["Brazil"]
print(countries_capitals)


 