def main():
    book_path = "books/frankenstein.txt.save"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sum_chars = get_sum_chars (text)
    print(f"{num_words} words found in the document")
    print(f"{sum_chars} letters found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars [lowered] += 1
        else:
            chars [lowered] = 1
    return chars

def get_sum_chars (text): 
      words = text.split()
      return len(words)          
        
        

main()
