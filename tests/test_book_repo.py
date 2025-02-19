from lib.book_repo import BookRepository
from lib.book import Book


"""
When we call the all() method on the book repo class
we get a list of books objects from the seed data
"""
def test_get_all_books(db_connection):
	db_connection.seed('seeds/book_store.sql')
	book_repo = BookRepository(db_connection)

	result = book_repo.all()

	assert result == [
		Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
		Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
		Book(3, 'Emma', 'Jane Austen'),
		Book(4, 'Dracula', 'Bram Stoker'),
		Book(5, 'The Age of Innocence', 'Edith Wharton')
	]

"""
when we search for book by id by calling find method
it returns a book object with the corresponding id
"""
def test_find_book_by_id(db_connection):
	db_connection.seed('seeds/book_store.sql')
	book_repo = BookRepository(db_connection)

	result = book_repo.find(book_id=4)

	assert result == Book(4, 'Dracula', 'Bram Stoker')