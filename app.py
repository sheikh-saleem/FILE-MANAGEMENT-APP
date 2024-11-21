import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found.")
    else:
        print("Files in directory:")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter data to append: ")
            f.write(content + "\n")
            print(f"Content added to '{filename}' successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nFILE MANAGEMENT APP")
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            filename = input("Enter the file name: ")
            create_file(filename)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            filename = input("Enter the name of the file to delete: ")
            delete_file(filename)
        elif choice == "4":
            filename = input("Enter the filename to read: ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter the filename to edit: ")
            edit_file(filename)
        elif choice == "6":
            print("Closing the app....")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()