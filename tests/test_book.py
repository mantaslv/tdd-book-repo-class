from lib.book import Book

"""
test initialise column names as variables
"""
def test_initialise_variables():
	book = Book(1, "test title", "test author")

	assert book.id == 1
	assert book.title == "test title"
	assert book.author_name == "test author"

"""
format book object as a string
"""
def test_formats_nicely():
	book = Book(1, "test title", "test author")
	
	assert str(book) == 'Book(1, test title, test author)'

"""
compare 2 books with same attributes and have them be equal
"""
def test_books_are_equal():
	book1 = Book(1, "test title", "test author")
	book2 = Book(1, "test title", "test author")

	assert book1 == book2
	