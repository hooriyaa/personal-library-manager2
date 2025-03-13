# import streamlit as st
# from app.crud import add_book, view_books, update_status, delete_book
# from app.utils import convert_to_dataframe

# st.title("📚 Personal Library Manager")

# menu = ["Add Book", "View Books", "Update Status", "Delete Book"]
# choice = st.sidebar.selectbox("Menu", menu)

# # 📌 Add Book
# if choice == "Add Book":
#     title = st.text_input("Book Title")
#     author = st.text_input("Author")
#     genre = st.text_input("Genre")
#     if st.button("Add Book"):
#         add_book(title, author, genre)
#         st.success("Book added successfully!")

# # 📌 View Books
# elif choice == "View Books":
#     books = view_books()
#     df = convert_to_dataframe(books)
#     st.dataframe(df)

# # 📌 Update Book Status
# elif choice == "Update Status":
#     books = view_books()
#     book_list = {f"{b[1]} by {b[2]}": b[0] for b in books}
#     selected_book = st.selectbox("Select Book", list(book_list.keys()))
#     new_status = st.radio("New Status", ["Available", "Checked Out"])

#     if st.button("Update Status"):
#         update_status(book_list[selected_book], new_status)
#         st.success("Book status updated!")

# # 📌 Delete Book
# elif choice == "Delete Book":
#     books = view_books()
#     book_list = {f"{b[1]} by {b[2]}": b[0] for b in books}
#     selected_book = st.selectbox("Select Book to Delete", list(book_list.keys()))

#     if st.button("Delete Book"):
#         delete_book(book_list[selected_book])
#         st.warning("Book deleted!")

import streamlit as st
import pandas as pd
from app.crud import add_book, remove_book, search_books, fetch_books
from app.utils import convert_to_dataframe

# 📌 Streamlit Page Configuration
st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖", layout="wide")
st.title("📖 My Digital Library")
st.markdown("Manage your books efficiently with this personal library manager. 📚")

# 📌 Sidebar Menu
menu = ["🏠 Home", "➕ Add a Book", "🗑 Remove a Book", "🔍 Search for a Book", "📖 Display All Books"]
choice = st.sidebar.radio("📌 Choose an option", menu)

# 📌 Home
if choice == "🏠 Home":
    st.image("bookshelf.jpg", width=600)
    st.markdown("**Easily track and organize your book collection!**")

# 📌 Add a Book
elif choice == "➕ Add a Book":
    st.subheader("📌 Add a New Book to Your Collection")
    title = st.text_input("📖 Title")
    author = st.text_input("✍️ Author")
    year = st.number_input("📅 Publication Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("📚 Genre")
    read_status = st.checkbox("✅ Mark as Read")
    rating = st.slider("⭐ Rating", min_value=0, max_value=5, step=1)
    summary = st.text_area("📝 Short Summary")

    if st.button("➕ Add Book"):
        add_book(title, author, year, genre, read_status, rating, summary)
        st.success(f'✔️ "{title}" has been added!')

# 📌 Remove a Book
elif choice == "🗑 Remove a Book":
    st.subheader("❌ Remove a Book")
    books_df = convert_to_dataframe(fetch_books())
    
    if not books_df.empty:
        selected_book = st.selectbox("🗂 Select a book to remove", books_df["Title"])
        if st.button("🗑 Remove Book"):
            remove_book(selected_book)
            st.success(f'❌ "{selected_book}" has been removed!')
    else:
        st.warning("No books in the library yet.")

# 📌 Search for a Book
elif choice == "🔍 Search for a Book":
    st.subheader("🔎 Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    query = st.text_input("🔍 Enter search query")

    if st.button("🔎 Search"):
        results = convert_to_dataframe(search_books(query, search_by))
        
        if not results.empty:
            st.dataframe(results)
        else:
            st.warning("No matching books found.")

# 📌 Display All Books
elif choice == "📖 Display All Books":
    st.subheader("📚 Your Library Collection")
    books_df = convert_to_dataframe(fetch_books())

    if not books_df.empty:
        st.dataframe(books_df)
    else:
        st.warning("Your library is empty. Start adding books!")

st.sidebar.markdown("📌 **Library data is saved automatically. Happy Reading!**")
