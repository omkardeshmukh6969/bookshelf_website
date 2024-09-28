import os

class Config:
    # Secret key for session management and other uses
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'

    # MySQL configurations
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'  # Replace with your MySQL username
    MYSQL_PASSWORD = 'Omkar@123'  # Replace with your MySQL password
    MYSQL_DB = 'bookshelf_db'  # We'll create this database soon
    MYSQL_CURSORCLASS = 'DictCursor'
