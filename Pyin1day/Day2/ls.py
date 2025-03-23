import os

# Function to list files in a given folder
def list_files_in_folder(folder_path):
    try:
        # Attempt to list files in the specified folder
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        # Return an error message if the folder is not found
        return None, "Folder not found"
    except PermissionError:
        # Return an error message if there is a permission issue
        return None, "Permission denied"

# Main function to handle user input and display files or errors
def main():
    # Prompt user to enter a list of folder paths separated by spaces
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    # Iterate over each folder path provided by the user
    for folder_path in folder_paths:
        # Get the list of files and any error message for the current folder path
        files, error_message = list_files_in_folder(folder_path)
        if files:
            # If files are found, print the folder path and list of files
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            # If an error occurred, print the folder path and the error message
            print(f"Error in {folder_path}: {error_message}")

# Entry point of the script
if __name__ == "__main__":
    main()