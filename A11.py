#Handling exceptions in Python

with open(r"C:\Users\Abhishek\OneDrive\Desktop\student.txt","r") as f1:
  content = f1.readline()
  print(content)
#read all lines into a list and print them
with open(r"C:\Users\Abhishek\OneDrive\Desktop\student.txt","r") as f1:
    content = f1.readlines()
    print(content)

    #loop through the list and print each line separately
    for line in content:
       print(line)
       #count the number of students in the file
       num_students = len(content)
       print("Number of stuedents:",num_students)

       #open student.txt in write mode and add 3 more students
with open(r"C:\Users\Abhishek\OneDrive\Desktop\student.txt","a") as f1:
     f1.write("\nnikhil")
     f1.write("\nrahul")
     f1.write("\nsachin")
print("3 students added successfully")
print(content)   

#after writing, open the file again in read mode and print its content
with open(r"C:\Users\Abhishek\OneDrive\Desktop\student.txt","r") as f1:
    content = f1.readlines()
    print(content)

    #open student.txt in append mode and add 2 more students

with open(r"C:\Users\Abhishek\OneDrive\Desktop\student.txt","a") as f1:
        f1.write("\npriya")
        f1.write("\nmeena")
print("2 students added successfully")
print(content)

#verify that the new student was added at the end 
with open(r"C:\Users\Abhishek\OneDrive\Desktop\student.txt","r") as f1:
    content = f1.readlines()
    print(content)
    