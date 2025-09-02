#1 Flight Booking
# flights = {}
# sub_dict = {}
#
# def book_seat(flights, flight_no, passenger):
#     if flight_no not in flights:
#         raise KeyError('Flight number not available!')
#     else:
#         value = flights[flight_no]['seats']
#         value -=1
#         flights[flight_no]['seats'] = value
#         flights[flight_no]['passengers'].append(passenger)
#     return flights
#
#
# while True:
#     flight_no = input("Flight no: ")
#     if flight_no == 'done':
#         break
#     sub_dict['seats'] = int(input("Number of seats: "))
#     sub_dict['passengers'] = []
#     flights[flight_no] = sub_dict
#     print()
#
# customer_flight = input("Enter the flight number to book: ")
# name_of_passenger = input("Enter the passenger name: ")
# print(book_seat(flights, customer_flight, name_of_passenger ))

#2
# my_tup = ()
# my_list = []
# while True :
#     n = int(input())
#     my_list.append(n)
#     if len(my_list) > 2:
#         my_list.pop(-1)
#         print('More than 3')
#         break
# my_tup = tuple(my_list)
# print(my_tup)

#3
# n = 20
# row = 1
# target = 20
#
# number = 1
# space = target -1
# while n >= number:
#     print(" " * space, end="")
#     for x in range(row):
#         if number > target:
#             break
#         print(number, end=" ")
#         number += 1
#     print()
#     space -=1
#     row += 1



#4
# my_list = [('gray',2), ('blue',4)]
# d  = {}
# for i in range (2):
#     for x in range(2):
#         my_tup.append(input('Input: '))
#     print (my_tup)
#     my_list.append(tuple(my_tup))
#     my_tup = []
# print(my_list)
#
# for i in my_list:
#     for j in range(len(i)):
#         if j == 0:
#             first = i[j]
#         elif j == 1:
#             d[first] = i[j]
#
# print(d)


# 5

# d = {
#  'a' : 1,
#  'b' : 2,
#  'c' : 3,
#  'd' : 4,
# }
#
# def get_tuple(dict, key):
#     if  key in d:
#         return (key, d[key])
#     else:
#         return (key, "Not found")
#
# print(get_tuple(d, 'a'))
# print(get_tuple(d, 'z'))

# 6
# d = {'a': 20,  'b': 10, 'c' : 30 }
# new_d = {}
# cutoff = 10
# def greater_dict(d, cutoff):
#     l = []
#     for k in d:
#         if d[k] > cutoff:
#             l.append(k)
#         else:
#             continue
#     for i in l:
#         new_d[i] = d[i]
#     return new_d


# print(greater_dict(d, cutoff))


# 7
# lit = ['a','b','a','c','b','a']
# seen = []
# counts = []
# d = {}
# def get_counts(lit):
#     for i in lit:
#         if i in seen:
#             continue
#         else:
#             seen.append(i)
#             counts.append(lit.count(i))
#     for x in range(len(seen)):
#         d[seen[x]] = counts[x]
#     return d

# print(get_counts(lit))

# class CustomException(Exception):
#     pass

# def divide(a,b):
#    if b==0:
#        raise CustomException('Cannot divide by zero')
#    return a/b

# try:
#     divide(10,0)
# except CustomException as e:
#     print(e)

