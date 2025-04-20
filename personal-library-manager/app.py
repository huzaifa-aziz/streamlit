import json

# Function to load library from a file
def load_library():
    try:
        with open('library.txt', 'r') as file:
            library = json.load(file)
    except FileNotFoundError:
        library = []
    return library

# Function to save library to a file
def save_library(library):
    with open('library.txt', 'w') as file:
        json.dump(library, file)

# Function to add a book to the library
def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the publication year of the book: "))
    genre = input("Enter the genre of the book: ")
    read_status = input("Has the book been read? (y/n): ").lower() == 'y'
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read_status': read_status
    }
    
    library.append(book)
    print("Book added successfully!")

# Function to remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    removed = False
    
    for book in library:
        if book['title'] == title:
            library.remove(book)
            removed = True
            print("Book removed successfully!")
            break
    
    if not removed:
        print("Book not found in the library.")

# Function to search for a book in the library
def search_book(library):
    keyword = input("Enter a keyword to search for: ")
    found_books = []
    
    for book in library:
        if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
            found_books.append(book)
    
    if found_books:
        print("Matching books:")
        for book in found_books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read Status: {'Read' if book['read_status'] else 'Unread'}")
            print()
    else:
        print("No matching books found.")

# Function to display all books in the library
def display_books(library):
    if library:
        print("All books in the library:")
        for book in library:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read Status: {'Read' if book['read_status'] else 'Unread'}")
            print()
    else:
        print("The library is empty.")

# Function to display library statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(book['read_status'] for book in library)
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print(f"Total books in the library: {total_books}")
    print(f"Percentage of books read: {percentage_read}%")

# Main program loop
def main():
    library = load_library()
    
    while True:
        print("Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
