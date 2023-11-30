from unittest import TestCase
from strlib import reverse


class TestTypes(TestCase):
    def test_set_type(self):
        with self.assertRaises(TypeError) as _:
            reverse(set())  # pyright: ignore (type error)

    def test_dict_type(self):
        with self.assertRaises(TypeError) as _:
            reverse(dict())  # pyright: ignore (type error)

    def test_int_type(self):
        with self.assertRaises(TypeError) as _:
            reverse(int())  # pyright: ignore (type error)

    def test_float_type(self):
        with self.assertRaises(TypeError) as _:
            reverse(float())  # pyright: ignore (type error)

    def test_boolean_type(self):
        with self.assertRaises(TypeError) as _:
            reverse(bool())  # pyright: ignore (type error)

    def test_tuple_type(self):
        with self.assertRaises(TypeError) as _:
            reverse(tuple())  # pyright: ignore (type error)
