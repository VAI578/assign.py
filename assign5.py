#task1
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eva": 88
}


name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found in the dictionary.")

    #task2
    
numbers = list(range(1, 11))


first_five = numbers[:5]

reversed_list = first_five[::-1]


print("Original list:", numbers)
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_list)