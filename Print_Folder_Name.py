def get_folder_name(operations):
    folder_to_file_names = {}
    for operation in operations:
        if operation.startswith("goto"):
            folder_name = operation[5:]
            folder_to_file_names[folder_name] = list()
        elif operation.startswith("create"):
            file_name = operation[7:]
            folder_to_file_names[folder_name].append(file_name)
    print(folder_to_file_names)

    # Core Logic Implementation
    for folder_name, file_names in folder_to_file_names.items():
        unique_file_names = list(set(file_names))
        if len(unique_file_names) == len(file_names) and len(file_names) >= 1:
            return folder_name
    return "None"


operations = [
    "goto folderA", "create fileA", "create fileB", "create fileA",
    "goto folderB",
    "goto folderC", "create fileA", "create fileB", "create fileC"
]
print(get_folder_name(operations))



operations2 = [
    "goto folderA", "create fileA", "create fileB",
    "create fileA", "create fileB", "goto folderB",
    "goto folderC", "create fileA", "create fileB", "create fileB"
]
print(get_folder_name(operations2))



operations3 = [
    "goto folderA",
    "goto folderB",
    "goto folderC", "create fileA", "create fileB", "create fileC"
]
print(get_folder_name(operations3))