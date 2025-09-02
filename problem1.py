# library = {
#     "Harry Potter" : 3,
#     "Nigga" : 2
# }

# def borrow_book(library, book):
#     if book not in library:
#         raise KeyError(f'{book} is not exist!')
#     if library[book] == 0:
#         raise Exception("Book not available")
    
#     library[book] -= 1
#     return library

# print(library)

# borrow_book(library, "Nigga")

# print(library)


# def safe_division(a, b):
#     if b == 0:
#         raise ZeroDivisionError('Zero Division Error')
    
#     if type(a) is not int or type(b) is not int:
#         raise TypeError("Input must be a number")
    
#     return (a//b, a%b)

# print(safe_division(5,0))

# flights = {
#     "FL123": {
#         "seats" : 2, 
#         "passengers": []
#     },
#     "FL456": {
#         "seats" : 2, 
#         "passengers": []
#     }
# }

# def book_seat(flights, flight_no, passenger):
#     if flight_no not in flights:
#         raise KeyError("Flight doesnt exist")    
#     if flights[flight_no]["seats"] == 0:
#         raise Exception("No seats available")  
#     flights[flight_no]["passengers"].append(passenger)
#     flights[flight_no]["seats"] -= 1
#     return flights

# book_seat(flights, "FL123", "Alice")
# book_seat(flights, "FL123", "Bob")
# print(flights)

# library = {
#     "Python Basics": ("John Doe", 2018, 3),
#     "Data Science 101": ("Jane Smith", 2020, 2),
#     "AI Revolution": ("Alan Turing", 2021, 1)
# }

# def add_books(**book_info):
#     title = book_info["title"]
#     author = book_info["author"]
#     year = book_info["year"]
#     copies = book_info.get("copies", 1)

#     if title in library:
#         print("Title already exist")
#     else:
#         library[title] = (author, year, copies)
#         print("Book added successfully")
    

# def search_books(*keywords):
#     results = []
#     for title in library:
#         for keyword in keywords:
#             if keyword.lower() in title.lower():
#                 results.append(title)
#                 break
#     return results
        
# def borrow_books(title):
#     try:
#         author, year, copies = library[title]
#         if copies > 0:
#             library[title] = (author, year, copies - 1)
#             print(f'You borrowed {title}. Copies left {copies - 1}')
#         else:
#             raise Exception("Book not avaible!")
#     except KeyError:
#         print("Book doesnt Exist")
        
# def return_books(title):
#     try:
#         author, year, copies = library[title]
#         library[title] = (author, year, copies + 1)
#         print("Book return")
#     except KeyError:
#         raise ValueError("Book not found")
    

# def display_library():
#     print("Book Collection:")
#     sorted_books = sorted(library.items(), key=lambda x: x[1][1])
#     for title, (author, year, copies) in sorted_books:
#         print(f"{title} - {author} ({year}) | Copies: {copies}")
#     print("-" * 50)
    
#add_books(title="Machine Learning", author="Andrew Ng", year=2019, copies=4)


#borrow_books("Python Basics")
#borrow_books("AI Revolution")
#borrow_books("AI Revolution")  


#return_books("AI Revolution")

#print(search_books("Python", "Data"))

#display_library()



# # Dictionary structure: { student_id: (name, age, grades) }
# students = {
#     "S001": ("Alice", 20, (90, 85, 92)),
#     "S002": ("Bob", 21, (78, 81, 86)),
#     "S003": ("Charlie", 19, (95, 90, 93))
# }


# # 1. Add a new student
# def add_student(student_id, name, age, *grades):
#     if student_id in students:
#         print(f"Student {student_id} already exists.")
#     else:
#         students[student_id] = (name, age, grades)
#         print(f"Student {student_id} added successfully!")


# # 2. Get average grade of a student
# def get_average(student_id):
#     try:
#         name, age, grades = students[student_id]
#         if not grades:
#             raise ValueError("No grades available")
#         return sum(grades) / len(grades)
#     except KeyError:
#         raise KeyError(f"Student {student_id} not found")


# # 3. Update grades of a student
# def update_grades(student_id, *new_grades):
#     try:
#         name, age, _ = students[student_id]
#         students[student_id] = (name, age, new_grades)
#         print(f"Grades updated for {student_id}")
#     except KeyError:
#         raise KeyError(f"Student {student_id} not found")


# # 4. Rank students by average grade (highest first)
# def rank_students():
#     ranked = sorted(
#         students.items(),
#         key=lambda x: sum(x[1][2]) / len(x[1][2]) if x[1][2] else 0,
#         reverse=True
#     )
#     return ranked


# # 5. Display students with averages
# def display_students():
#     print("\n🎓 Student Records:")
#     for student_id, (name, age, grades) in rank_students():
#         try:
#             avg = get_average(student_id)
#             print(f"ID: {student_id} | Name: {name} | Age: {age} "
#                   f"| Grades: {grades} | Average: {avg:.2f}")
#         except ValueError as e:
#             print(f"ID: {student_id} | Name: {name} | Age: {age} "
#                   f"| Grades: {grades} | Error: {e}")
#     print("-" * 60)


# # -------------------------
# # Example Usage
# # -------------------------

# # Add a new student
# add_student("S004", "Diana", 22, 88, 91, 85)

# # Update Bob's grades
# update_grades("S002", 90, 89, 87)

# # Try updating a non-existent student
# try:
#     update_grades("S999", 100)
# except KeyError as e:
#     print(f"Error: {e}")

# # Display final records
# display_students()