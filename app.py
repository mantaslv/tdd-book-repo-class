from lib.database_connection import DatabaseConnection
from lib.book_repo import BookRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all artists
book_repo = BookRepository(connection)
books = book_repo.all()

# List them out
for book in books:
    print(book)

print('\n')

print(book_repo.find(2))
