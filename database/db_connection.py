import mysql.connector
# 📌 Connect to MySQL Database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Update as per your credentials
        password="guujarMahnoor@123",
        database="library_manager_db",
        auth_plugin='mysql_native_password'
    )

