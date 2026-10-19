
from book import Book
from user import User
from library import Library

def test_borrow_book_integration():
    library = Library()

    book = Book("1984", "George Orwell", 1949, "ISBN001")
    user = User("Daniela", "U001")

    library.add_book(book)
    library.add_user(user)

    library.borrow_book("U001", "ISBN001")

    assert book.borrowed == True
    assert user.history == ["Borrowed: 1984"]

    
def test_borrow_book_twice_integration():
    import pytest

    library = Library()

    book = Book("1984", "George Orwell", 1949, "ISBN001")
    user = User("Daniela", "U001")

    library.add_book(book)
    library.add_user(user)

    library.borrow_book("U001", "ISBN001")

    with pytest.raises(ValueError):
        library.borrow_book("U001", "ISBN001")

    assert book.borrowed == True
    assert user.history == ["Borrowed: 1984"]

