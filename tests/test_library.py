import unittest
from src.library import Library

class TestLibrary(unittest.TestCase):

    # -------- Sprint 1 --------
    def test_add_book_success(self):
        lib = Library()
        lib.add_book("1", "C++", "Bjarne")
        self.assertEqual(len(lib.books), 1)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book("1", "C++", "Bjarne")
        with self.assertRaises(ValueError):
            lib.add_book("1", "Python", "Guido")

    # -------- Sprint 2 --------
    def test_borrow_book(self):
        lib = Library()
        lib.add_book("1", "C++", "Bjarne")
        lib.borrow_book("1")
        self.assertTrue(lib.books["1"].borrowed)

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("1", "C++", "Bjarne")
        lib.borrow_book("1")
        with self.assertRaises(ValueError):
            lib.borrow_book("1")

    def test_return_book(self):
        lib = Library()
        lib.add_book("1", "C++", "Bjarne")
        lib.borrow_book("1")
        lib.return_book("1")
        self.assertFalse(lib.books["1"].borrowed)

    # -------- Sprint 3 --------
    def test_report_has_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("BookID", report)

    def test_report_has_entry(self):
        lib = Library()
        lib.add_book("1", "C++", "Bjarne")
        report = lib.generate_report()
        self.assertIn("C++", report)


if __name__ == "__main__":
    unittest.main()
