import book
import pytest
import library
import user


# PRUEBA ORIGINAL: comprobar que el libro se puede prestar.
@pytest.mark.unit
def test_borrow_book():
    book1 = book.Book(
        "El alquimista", "Paulo Coelho", "1967", "ISBN001"
    )
    assert book1.title == "El alquimista"

    book1.borrow()

    # True significa que el libro está prestado.
    assert book1.borrowed == True


# PRUEBA ORIGINAL: intentar prestar un libro ya prestado.
@pytest.mark.wip
def test_re_borrow():
    book1 = book.Book(
        "El alquimista", "Paulo Coelho", "1967", "ISBN001"
    )
    book1.borrow()

    # La prueba pasa si el segundo préstamo lanza este error.
    with pytest.raises(
        ValueError, match="The book is already borrowed"
    ):
        book1.borrow()


# PRUEBA ORIGINAL: prestar y devolver el libro.
# Se corrigió el marcador: esta prueba es unitaria.
@pytest.mark.unit
def test_re_borrow_and_book():
    book1 = book.Book(
        "El alquimista", "Paulo Coelho", "1967", "ISBN001"
    )

    book1.borrow()
    assert book1.borrowed == True

    book1.return_book()
    assert book1.borrowed == False


# PRUEBA ORIGINAL: comprobar que biblioteca, libro y usuario
# trabajan juntos para realizar el préstamo.
@pytest.mark.m
def test_library_borrow():
    book1 = book.Book(
        "El alquimista", "Paulo Coelho", "1967", "ISBN001"
    )
    Miguel = user.User("Miguel", "ID001")

    libro = library.Library()
    libro.add_book(book1)
    assert libro.books[0].title == "El alquimista"

    libro.add_user(Miguel)
    libro.borrow_book("ID001", "ISBN001")

    assert book1.borrowed == True


# FIXTURE ORIGINAL: prepara una biblioteca con libro y usuario.
@pytest.fixture
def library_init():
    book1 = book.Book(
        "El alquimista", "Paulo Coelho", "1967", "ISBN001"
    )
    Miguel = user.User("Miguel", "ID001")

    libro = library.Library()
    libro.add_book(book1)
    libro.add_user(Miguel)

    # CORRECCIÓN: entregar la biblioteca a quien use la fixture.
    return libro


# PRUEBA ORIGINAL: usar la biblioteca preparada por la fixture.
@pytest.mark.wip
def test_library(library_init):
    libro = library_init

    # CORRECCIÓN: usar exactamente los identificadores registrados.
    libro.borrow_book("ID001", "ISBN001")

    assert libro.books[0].borrowed == True


# NUEVA 1 - PARAMETRIZE:
# Ejecuta la misma prueba tres veces, una por cada nombre.
@pytest.mark.parametrize("nombre", ["Dani", "Miguel", "Anna"])
def test_crear_usuario(nombre):
    usuario = user.User(nombre, "ID001")

    assert usuario.name == nombre
    assert usuario.history == []


# NUEVA 2 - MONKEYPATCH.SETATTR:
# Cambia temporalmente un atributo para simular un libro prestado.
def test_monkeypatch_setattr(monkeypatch):
    book1 = book.Book("1984", "George Orwell", 1949, "ISBN002")

    monkeypatch.setattr(book1, "borrowed", True)

    # Como simulamos que ya está prestado, debe lanzar ValueError.
    with pytest.raises(
        ValueError, match="The book is already borrowed"
    ):
        book1.borrow()


# NUEVA 3 - MONKEYPATCH.DELATTR:
# Elimina temporalmente el atributo borrowed.
def test_monkeypatch_delattr(monkeypatch):
    book1 = book.Book("1984", "George Orwell", 1949, "ISBN002")

    monkeypatch.delattr(book1, "borrowed")

    # borrow() intenta usar ese atributo y debe lanzar AttributeError.
    with pytest.raises(AttributeError):
        book1.borrow()


# NUEVA 4: comprobar que get_history() devuelve una lista vacía
# cuando el usuario todavía no tiene movimientos.
def test_historial_vacio():
    usuario = user.User("Dani", "ID002")

    assert usuario.get_history() == []


# NUEVA 5: comprobar el error al solicitar un libro inexistente.
# Reutiliza la fixture para tener una biblioteca preparada.
def test_libro_inexistente(library_init):
    with pytest.raises(ValueError, match="Book not found"):
        library_init.borrow_book("ID001", "NOEXISTE")