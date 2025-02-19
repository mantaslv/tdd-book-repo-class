from .book import Book

class BookRepository:
	def __init__(self, connection):
		self._connection = connection

	def all(self):
		rows = self._connection.execute('SELECT * FROM books')
		result = []
		for row in rows:
			item = Book(row["id"], row["title"], row["author_name"])
			result.append(item)
		return result

	def find(self, book_id):
		rows = self._connection.execute('SELECT * FROM books WHERE id = %s', [book_id])
		row = rows[0]
		return Book(row["id"], row["title"], row["author_name"])
