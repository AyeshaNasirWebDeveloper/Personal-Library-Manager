import streamlit as st
import json

LIBRARY_FILE = "library.json"

def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library, title, author, year, genre, read):
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
    save_library(library)

def remove_book(library, title):
    updated_library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(updated_library)
    return updated_library

def search_books(library, keyword):
    return [book for book in library if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]

def display_stats(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    return total_books, percentage_read

st.title("📚 Personal Library Manager")
library = load_library()

menu = st.sidebar.radio("Menu 📝", ["Add Book", "Remove Book", "Search Book", "Display All Books", "Statistics"])

if menu == "Add Book":
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Read")
    if st.button("Add Book"):
        add_book(library, title, author, year, genre, read)
        st.success("Book added successfully!")

elif menu == "Remove Book":
    title = st.text_input("Enter book title to remove")
    if st.button("Remove Book"):
        library = remove_book(library, title)
        st.success("Book removed successfully!")

elif menu == "Search Book":
    keyword = st.text_input("Search by title or author")
    if st.button("Search"):
        results = search_books(library, keyword)
        if results:
            for book in results:
                st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found.")

elif menu == "Display All Books :books:":
    if library:
        for book in library:
            st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        st.info("No books in the library yet.")

elif menu == "Statistics":
    total, percentage = display_stats(library)
    st.write(f"Total books: {total}")
    st.write(f"Percentage read: {percentage:.2f}%")

st.sidebar.write("📌 Library data is automatically saved.")
