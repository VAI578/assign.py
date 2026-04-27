# Task 1: Read a File and Handle Errors
#
try:
    
    file = open("sample.txt", "r")

    print("File content:\n")

  
    for line in file:
        print(line.strip())
        
        
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

except Exception as e:
    print("An unexpected error occurred:", e)

    # task 2

    # Write and Append Data to a File

# Step 1: Take input and write to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.\n")

# Step 2: Append additional data
more_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(more_text + "\n")

print("Data successfully appended.\n")

# Step 3: Read and display final content
print("Final content of output.txt:")

with open("output.txt", "r") as file:
    print(file.read())
