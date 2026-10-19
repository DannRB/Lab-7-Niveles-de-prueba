
from book import Book
from user import User

def test_create_book():
    book = Book("1984", "George Orwell", 1949, "ISBN001")

    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.year == 1949
    assert book.isbn == "ISBN001"
    assert book.borrowed == False

    
def test_borrow_book():
    book = Book("1984", "George Orwell", 1949, "ISBN001")

    book.borrow()

    assert book.borrowed == True

    
def test_borrow_book_already_borrowed():
    import pytest

    book = Book("1984", "George Orwell", 1949, "ISBN001")

    book.borrow()

    with pytest.raises(ValueError):
        book.borrow()


def test_return_book():
    book = Book("1984", "George Orwell", 1949, "ISBN001")

    book.borrow()

    book.return_book()

    assert book.borrowed == False

    
def test_register_borrow():
    book = Book("1984", "George Orwell", 1949, "ISBN001")
    user = User("Daniela", "U001")

    user.register_borrow(book)

    assert user.history == ["Borrowed: 1984"]



