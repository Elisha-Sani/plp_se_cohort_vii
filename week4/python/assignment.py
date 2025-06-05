# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.


# Read User File
def read_file():
        f_name = input("Enter file name: ")
        file_name = f_name + ".txt"
        try:
            with open(file_name, "r") as myfile:
                data = myfile.read()
                print("------FILE CONTENT------")
                print(data)
                print("---------------------------\n")
                return(data)
        except FileNotFoundError:
            print("File Does Not Exist")
            return None

# Modify File
def modify_file():
    mod_content = input("Enter the Your new modifications here: \n")
    m_name = input("Enter the name of the new file: ")
    mod_name = m_name + ".txt"
    try:
        with open(mod_name, "w") as newfile:
            newfile.write(mod_content)
        print(f"File modified sucessfully and saved as: {mod_name}")
    except OSError:
        print("Failed to Create File")


# Main Program
user_input = input("Do you want to read file: (y)/(n): ").lower().strip()
if user_input == "n":
    print("See you later")
else:
    result = read_file()
    if result is not None:
        user_input = input("Do you want to modify: (y)/(n): ").lower().strip()
        if user_input == "n":
            print("See you later")
        else:
            modify_file()    