#topen product text file read mode and display all product records

with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "r") as f1:
	content = f1.readline()
	print(content)
	
    #read and print only the first product from the list 
	first_product = content[0]
	
    #read all lines into a list and print the list
	with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "r") as f1:
		content = f1.readlines()
		print(content)
		
        #read the file line by line using a loop
		for line in content:
			print(line)
		#count the total number of products in the file
		Total_products = len(content)
		print("total number of products :", Total_products)
		#display only the products names from the file 
		for line in content:
			products_details = line.split(",")
			print("Product Name :", products_details[1])
			
            #Display products whose price is greater than 10000
			for line in content:
				products_details = line .split(",")
				if float(products_details[2]) > 10000:
					print("Product Name :", products_details[1])
					
              #open text file in write mode and write the following new data into it
#P201,Headphones,2000,Electronics     
#P202,sofa,28000,Furniture
#P203,printer,12000,Electronics

with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "w") as f1:
      f1.write("P201,Headphones,2000,Electronics\n")
      f1.write("P202,sofa,28000,Furniture\n")
      f1.write("P203,printer,12000,Electronics\n")
	  
      #after writing reopen the file and display its content
with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "r") as f1:
      content = f1.read()
      print(content)
	  
      #open the file in append mode and add the products
with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "a") as f1:
        f1.write("P204,Tablet,15000,Electronics\n")
        f1.write("P205,Dining Table,35000,Furniture\n")
        f1.write("P206,Smartwatch,8000,Electronics\n")
		
        #verify that the new products added at the end of the file
with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "r") as f1:
    
        content = f1.read()
print(content)

#open the file in r+ mode and update the name "Mouse" to "Wireless Mouse" 
with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "r+") as f1:
    content = f1.readlines()
    f1.seek(0)
    for line in content:
        if "Mouse" in line:
            line = line.replace("Mouse", "Wireless Mouse")
        f1.write(line)
    f1.truncate()
    
    #using r+ modem, move the cursor to the end of the file and add
with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "r+") as f1:
    f1.seek(0, 2)  # Move the cursor to the end of the file
    f1.write("P207,Gaming Console,25000,Electronics\n")
    f1.write("P208,Bookshelf,12000,Furniture\n")

    #count how many products belong to the category "Electronics"
with open(r"C:\Users\Abhishek\OneDrive\Desktop\laptopwaliDukan.txt", "r") as f1:
    content = f1.readlines()
    electronics_count = 0
    for line in content:
        products_details = line.split(",")
        if products_details[3].strip() == "Electronics":
            electronics_count += 1
    print("Total number of Electronics products:", electronics_count)



    #create a new text file expensive.txt and write only those products whose price is greater than 20000
with open(r"C:\Users\Abhishek\OneDrive\Desktop\expensive.txt", "w") as f2:
        for line in content:
            products_details = line.split(",")
            if float(products_details[2]) > 20000:
                f2.write(line)
