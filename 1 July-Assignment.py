#!/usr/bin/env python
# coding: utf-8

# # Q1. What is the primary goal of Object-Oriented Programming (OOP)?

# The primary goal of Object-Oriented Programming (OOP) is to bind together the data and the functions that operate on them, and to hide the details that are not relevant to other parts of the code1. This is also known as encapsulation, which is one of the four principles of OOP. The other three principles are inheritance, polymorphism, and abstraction.
# 
# OOP is a programming paradigm that uses objects as the primary source to implement real-world entities and concepts in code. Objects are data fields that have unique attributes and behavior, and can be created from reusable blueprints called classes. The purpose of OOP is to make the code more modular, reusable, and maintainable.

# # Q2. What is an object in Python?

# An object in Python is an instance of a class that has its own attributes and methods. A class is like a blueprint or a template that defines the common characteristics and behaviors of the objects that belong to it. For example, you can create a class called Car that has attributes like model, color, price, etc. and methods like start, stop, accelerate, etc. Then you can create different objects of the Car class, such as Audi, BMW, Tesla, etc. Each object will have its own values for the attributes and can use the methods defined in the class.
# 
# Objects are useful because they allow you to model real-world entities and concepts in your code. They also make your code more modular, reusable, and maintainable. You can create multiple objects of the same class without repeating the code for each one. You can also inherit the attributes and methods from one class to another, which is called inheritance. This way, you can create new classes that extend or modify the existing ones>

# In[7]:


# Define a class called Car
class Car:
    # Define the __init__ method that runs when an object is created
    def __init__(self, model, color, price):
        # Assign values to the attributes of the object
        self.model = model
        self.color = color
        self.price = price

    # Define a method that prints the details of the object
    def show_details(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")

# Create an object of the Car class
audi = Car("R8", "red", 100000)

# Call the show_details method on the object
audi.show_details()


# # Q3. What is a class in Python?

# A class in Python is a user-defined blueprint or prototype from which objects are created. Objects are data structures that have their own attributes and methods, which can be used to model real-world entities and concepts. A class defines the common characteristics and behaviors of the objects that belong to it, such as their data fields and functions.
# 
# For example, you can create a class called Animal that has attributes like name, color, age, etc. and methods like eat, sleep, make_sound, etc. Then you can create different objects of the Animal class, such as dog, cat, bird, etc. Each object will have its own values for the attributes and can use the methods defined in the class.
# 
# 

# # Q4. What are attributes and methods in a class?

# Attributes and methods are two important concepts in object-oriented programming. They are both related to classes, which are blueprints or templates for creating objects. Objects are data structures that have their own characteristics and behaviors, which can be used to model real-world entities and concepts.
# 
# Attributes are variables that are defined in a class and store some values for the objects. They represent the state or properties of the objects. For example, if you have a class called Person, you can define attributes like name, age, height, weight, etc. for each person object. Attributes can be either class attributes or instance attributes. Class attributes are shared by all objects of the same class, while instance attributes are unique to each object.
# 
# Methods are functions that are defined in a class and perform some actions on the objects. They represent the behavior or functionality of the objects. For example, if you have a class called Person, you can define methods like greet, walk, eat, sleep, etc. for each person object. Methods can access or modify the attributes of the objects or return some values. Methods usually have a special parameter called self, which refers to the current object that calls the method.

# # Q5. What is the difference between class variables and instance variables in Python?
# 

# Class variables and instance variables are two types of variables that can be used in Python classes. They differ in how they are defined, accessed, and shared among the objects of the class. Here are some of the main differences between them:
# 
# Class variables are declared within the class and outside any method. They are shared by all objects of the class and have the same value for every instance. Instance variables are declared inside a method and prefixed with self. They are unique to each object and can have different values for different instances.
# Class variables can be accessed by using the class name or the object name, followed by a dot and the variable name. For example, Car.count or audi.count. Instance variables can only be accessed by using the object name, followed by a dot and the variable name. For example, audi.model or audi.color.
# Class variables are usually used to store constants or values that are common to all objects of the class. For example, you can use a class variable to count how many objects of a class have been created. Instance variables are usually used to store attributes or properties that vary from one object to another. For example, you can use instance variables to store the model, color, and price of each car object.
# Class variables can be modified by using the class name or any object name, followed by a dot and the assignment operator. For example, Car.count = 10 or audi.count = 10. However, modifying a class variable through an object will create a new instance variable with the same name and hide the class variable for that object. Instance variables can be modified by using the object name, followed by a dot and the assignment operator. For example, audi.model = "A4" or audi.color = "blue".

# # Q6. What is the purpose of the self parameter in Python class methods?

# The self parameter in Python class methods is used to refer to the current instance of the class and access its attributes and methods. It is similar to the this keyword in other programming languages, but it is not a reserved word in Python. The self parameter is required as the first argument of any instance method definition, and it is passed implicitly when the method is called on an object.
# 
# The purpose of the self parameter is to allow Python to use the same syntax for accessing instance attributes and methods as for accessing global or local variables and functions. Python does not have any special notation or operator for referring to instance members, unlike some other languages that use a dot (.) or an at sign (@) for this purpose. Therefore, Python needs a way to distinguish between instance members and other variables or functions in the same scope. By using the self parameter, Python can access the instance members by prefixing them with self, and access other variables or functions by their names without any prefix.

# # Q7. For a library management system, you have to design the "Book" class with OOP principles in mind. The “Book” class will have following attributes:
# ###  a. title: Represents the title of the book.
# ###  b. author: Represents the author(s) of the book.
# ###  c. isbn: Represents the ISBN (International Standard Book Number) of the book.
# ###  d. publication_year: Represents the year of publication of the book.
# ###  e. available_copies: Represents the number of copies available for checkout. 
# ## The class will         also include the following methods:
# ###  a. check_out(self): Decrements the available copies by one if there are copies available for checkout.
# ###  b. return_book(self): Increments the available copies by one when a book is returned.
# ###  c. display_book_info(self): Displays the information about the book, including its attributes and the number of available copies.

# In[10]:


# Define a class called Book
class Book:
    # Define the __init__ method that runs when an object is created
    def __init__(self, title, author, isbn, publication_year, available_copies):
        # Assign values to the attributes of the object
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.available_copies = available_copies

    # Define a method that decrements the available copies by one if there are copies available for checkout
    def check_out(self):
        # Check if there are copies available for checkout
        if self.available_copies > 0:
            # Decrement the available copies by one
            self.available_copies -= 1
            # Print a message to confirm the checkout
            print(f"You have checked out {self.title} by {self.author}.")
        else:
            # Print a message to inform that there are no copies available for checkout
            print(f"Sorry, there are no copies of {self.title} by {self.author} available for checkout.")

    # Define a method that increments the available copies by one when a book is returned
    def return_book(self):
        # Increment the available copies by one
        self.available_copies += 1
        # Print a message to confirm the return
        print(f"You have returned {self.title} by {self.author}.")

    # Define a method that displays the information about the book, including its attributes and the number of available copies
    def display_book_info(self):
        # Print the information about the book in a formatted way
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Available Copies: {self.available_copies}")


# # Q8. For a ticket booking system, you have to design the "Ticket" class with OOP principles in mind. The “Ticket” class should have the following attributes:
# ### a. ticket_id: Represents the unique identifier for the ticket.
# ### b. event_name: Represents the name of the event.
# ### c. event_date: Represents the date of the event.
# ### d. venue: Represents the venue of the event.
# ### e. seat_number: Represents the seat number associated with the ticket.
# ### f. price: Represents the price of the ticket.
# ### g. is_reserved: Represents the reservation status of the ticket.
# ## The class also includes the following methods:
# ### a. reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
# ### b. cancel_reservation(self): Cancels the reservation of the ticket if it is already reserved.
# ### c. display_ticket_info(self): Displays the information about the ticket, including its attributes and reservation status.

# In[11]:


# Define a class called Ticket
class Ticket:
    # Define the __init__ method that runs when an object is created
    def __init__(self, ticket_id, event_name, event_date, venue, seat_number, price):
        # Assign values to the attributes of the object
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.seat_number = seat_number
        self.price = price
        # Initialize the reservation status of the ticket to False
        self.is_reserved = False

    # Define a method that marks the ticket as reserved if it is not already reserved
    def reserve_ticket(self):
        # Check if the ticket is already reserved
        if self.is_reserved:
            # Print a message to inform that the ticket is already reserved
            print(f"Sorry, this ticket (ID: {self.ticket_id}) is already reserved.")
        else:
            # Mark the ticket as reserved
            self.is_reserved = True
            # Print a message to confirm the reservation
            print(f"Congratulations, you have reserved this ticket (ID: {self.ticket_id}) for {self.event_name} on {self.event_date} at {self.venue}. Your seat number is {self.seat_number} and your price is ${self.price}.")

    # Define a method that cancels the reservation of the ticket if it is already reserved
    def cancel_reservation(self):
        # Check if the ticket is already reserved
        if self.is_reserved:
            # Mark the ticket as not reserved
            self.is_reserved = False
            # Print a message to confirm the cancellation
            print(f"You have cancelled your reservation for this ticket (ID: {self.ticket_id}) for {self.event_name} on {self.event_date} at {self.venue}.")
        else:
            # Print a message to inform that the ticket is not reserved
            print(f"Sorry, this ticket (ID: {self.ticket_id}) is not reserved.")

    # Define a method that displays the information about the ticket, including its attributes and reservation status
    def display_ticket_info(self):
        # Print the information about the ticket in a formatted way
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Venue: {self.venue}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: ${self.price}")
        print(f"Reservation Status: {'Reserved' if self.is_reserved else 'Not Reserved'}")


# # Q9. You are creating a shopping cart for an e-commerce website. Using OOP to model the "ShoppingCart" functionality the class should contain following attributes and methods:
# ### a. items: Represents the list of items in the shopping cart.
# 
# ## The class also includes the following methods:
# 
# ### a. add_item(self, item): Adds an item to the shopping cart by appending it to the list of items.
# ### b. remove_item(self, item): Removes an item from the shopping cart if it exists in the list.
# ### c. view_cart(self): Displays the items currently present in the shopping cart.
# ### d. clear_cart(self): Clears all items from the shopping cart by reassigning an empty list to the items attribute.

# In[13]:


# Define a class called ShoppingCart
class ShoppingCart:
    # Define the __init__ method that runs when an object is created
    def __init__(self):
        # Initialize the items attribute as an empty list
        self.items = []

    # Define a method that adds an item to the shopping cart by appending it to the list of items
    def add_item(self, item):
        # Append the item to the list of items
        self.items.append(item)
        # Print a message to confirm the addition
        print(f"You have added {item} to your shopping cart.")

    # Define a method that removes an item from the shopping cart if it exists in the list
    def remove_item(self, item):
        # Check if the item is in the list of items
        if item in self.items:
            # Remove the item from the list of items
            self.items.remove(item)
            # Print a message to confirm the removal
            print(f"You have removed {item} from your shopping cart.")
        else:
            # Print a message to inform that the item is not in the shopping cart
            print(f"Sorry, {item} is not in your shopping cart.")

    # Define a method that displays the items currently present in the shopping cart
    def view_cart(self):
        # Check if the list of items is empty
        if not self.items:
            # Print a message to inform that the shopping cart is empty
            print("Your shopping cart is empty.")
        else:
            # Print a message to show the items in the shopping cart
            print("Your shopping cart contains:")
            # Loop through each item in the list of items
            for item in self.items:
                # Print the item name
                print(f"- {item}")

    # Define a method that clears all items from the shopping cart by reassigning an empty list to the items attribute
    def clear_cart(self):
        # Reassign an empty list to the items attribute
        self.items = []
        # Print a message to confirm the clearing
        print("You have cleared your shopping cart.")


# # Q10. Imagine a school management system. You have to design the "Student" class usingOOP concepts.The “Student” class has the following attributes:
# ### a. name: Represents the name of the student.
# ### b. age: Represents the age of the student.
# ### c. grade: Represents the grade or class of the student.
# ### d. student_id: Represents the unique identifier for the student.
# ### e. attendance: Represents the attendance record of the student.
# ## The class should also include the following methods:
# ### a. update_attendance(self, date, status): Updates the attendance record of the student for a given date with the provided status (e.g., present or absent).
# ### b. get_attendance(self): Returns the attendance record of the student.
# ### c. get_average_attendance(self): Calculates and returns the average attendance percentage of the student based on their attendance record.

# In[15]:


# Define a class called Student
class Student:
    # Define the __init__ method that runs when an object is created
    def __init__(self, name, age, grade, student_id):
        # Assign values to the attributes of the object
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        # Initialize the attendance attribute as an empty dictionary
        self.attendance = {}

    # Define a method that updates the attendance record of the student for a given date with the provided status
    def update_attendance(self, date, status):
        # Check if the date is valid
        if isinstance(date, str) and len(date) == 10 and date[4] == "-" and date[7] == "-":
            # Check if the status is valid
            if status.lower() in ["present", "absent"]:
                # Update the attendance dictionary with the date and status as key-value pair
                self.attendance[date] = status.lower()
                # Print a message to confirm the update
                print(f"You have updated {self.name}'s attendance for {date} as {status.lower()}.")
            else:
                # Print a message to inform that the status is invalid
                print(f"Sorry, {status} is not a valid status. Please enter either 'present' or 'absent'.")
        else:
            # Print a message to inform that the date is invalid
            print(f"Sorry, {date} is not a valid date. Please enter in YYYY-MM-DD format.")

    


# In[ ]:




