def main():
    book_path = input ("Enter the file location:")
    book_text = get_book_text(book_path)
    print (book_text)
    print ("******************Next, test will become lowercase\n"
           "***************************************************\n"
           "***************************************************\n"
           "***************************************************\n"
           "***************************************************\n"
           "***************************************************\n"
           "***************************************************\n")
    
    make_lowerCase_letters (book_text)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    
def get_book_text (*arg):
    with open (*arg) as f:
        return f.read()
    
def make_lowerCase_letters (book_text):
    words = book_text.lower()
    return print(words)

def get_num_words (book_text):
    words = book_text.split()
    return len (words)
main()