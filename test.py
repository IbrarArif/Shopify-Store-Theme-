import os

def print_file_structure(folder_path, indent=0):
    try:
        items = os.listdir(folder_path)
    except PermissionError:
        print(" " * indent + "[Permission Denied]")
        return

    for item in items:
        item_path = os.path.join(folder_path, item)
        print(" " * indent + "|-- " + item)
        if os.path.isdir(item_path):
            print_file_structure(item_path, indent + 4)

if __name__ == "__main__":
    folder = r"H:\Smile-15-2-8\new-new"
    if os.path.exists(folder) and os.path.isdir(folder):
        print_file_structure(folder)
    else:
        print("Invalid folder path.")
