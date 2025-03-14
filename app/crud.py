from database.db_connection import get_db_connection

# 📌 Add a Book to Database
def add_book(title, author, year, genre, read_status, rating, summary):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO books (title, author, publication_year, genre, status, rating, summary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (title, author, year, genre, "Available" if read_status else "Checked Out", rating, summary))

    connection.commit()
    cursor.close()
    connection.close()

# 📌 Remove a Book by Title
def remove_book(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE Title = %s", (title,))
    conn.commit()
    conn.close()

# 📌 Search Books
def search_books(query, search_by):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM books WHERE {search_by} LIKE %s", (f"%{query}%",))
    data = cursor.fetchall()
    conn.close()
    return data

# 📌 Fetch All Books
def fetch_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    conn.close()
    return data
