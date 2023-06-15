def display_file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)
