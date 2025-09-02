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
