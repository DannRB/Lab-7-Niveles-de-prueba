import book
import pytest
import library
import user

@pytest.mark.unit
def test_borrow_book():
    book1= book.Book('El alquimista','Paulo Coehlo','1967','ISBN0001')
    assert book1.title =='El alquimista'
    book1.borrow()
    assert book1.borrowed ==True

@pytest.mark.wip
def test_re_borrow_book():
    book1= book.Book('El alquimista','Paulo Coehlo','1967','ISBN0001')
    assert book1.title =='El alquimista'
    book1.borrow()
    assert book1.borrowed ==True
    with pytest.raises(ValueError,match="The book is already borrowed"):
     book1.borrow()


@pytest.mark.system
def test_re_borrow_and_book():
    book1= book.Book('El alquimista','Paulo Coehlo','1967','ISBN0001')
    assert book1.title =='El alquimista'
    book1.borrow()
    assert book1.borrowed ==True
    book1.return_book()
    assert book1.borrowed == False


   

@pytest.mark.m
def test_library_borrow():
   book1= book.Book('El alquimista','Paulo Coehlo','1967','ISBN0001')
   Miguel = user.User('Miguel','ID001')

   libro = library.Library()
   libro.add_book(book1)
   assert libro.books[0].title == 'El alquimista'
   libro.add_user(Miguel)
   #corroborar que se agrego 
   libro.borrow_book('ID001','ISBN0001')
   assert book1.borrowed == True


@pytest.fixture 
def library_init():
   book1= book.Book('El alquimista','Paulo Coehlo','1967','ISBN0001')
   Miguel = user.User('Miguel','ID001')

   libro = library.Library()
   libro.add_book(book1)
   libro.add_user(Miguel)
@pytest.mark.wip
def test_library(library_init):
   libro= library_init
   #corroborar que se agrego 
   libro.borrow_book('ID0001','ISBN0001')
   assert libro.books[0].borrowed == True
