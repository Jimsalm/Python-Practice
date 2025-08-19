

assignment = []

print(f'Student Grade Calculator\n------------------------------------\n\n')

while True:
    
    user_input = input("Enter score: ")
    
    if user_input == 'done':
        break
    else:
        assignment.append(int(user_input))
        
print(f'Calculating Final Grade...\n------------------------------------\n')
print(f'Total Assignment: {len(assignment)}')

average_score = 0
for i in assignment:
    average_score += i

average = average_score / len(assignment)
print(f'Average Score: {average:.2f}')

final_grade = ''
if average_score >= 90 or average_score <= 100:
    final_grade = 'A'
elif average_score >= 80 or average_score <= 89:
     final_grade = 'B'    
elif average_score >= 70 or average_score <= 79:
     final_grade = 'C'     
elif average_score >= 60 or average_score <= 69:
     final_grade = 'D'
     
          
print(f'Total Grade: {final_grade}')