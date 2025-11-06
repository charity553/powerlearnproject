# Task 1
#  Create a program that reads a file and writes a modified version to a new file.
def modify_file(input_file, output_file):
    try:
        # Open and read input file
        with open(input_file, "r") as infile:
            content = infile.read()
        
        # Modify the content (make everything uppercase)
        modified_content = content.upper()
        
        # Write modified content to new file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"File has been modified and saved as '{output_file}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



modify_file("input.txt", "output.txt")

# Task 2
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def safe_file_reader():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, "r") as file:
            print("\n--- File Contents ---")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Run the function
safe_file_reader()
