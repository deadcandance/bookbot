
book_path = input ("Enter the file location:")
with open (book_path) as f:
    file_contents = f.read()
print (file_contents)