"""
python `which nosetests` -s supervision_1/test_question_4.py
"""

import unittest
import doctest
from show import show

from supervision_1 import question_4
from supervision_1.question_4 import Document, VSM
from supervision_1 import documents

class TestDoctests(unittest.TestCase):

    def test_doctests(self):
        doctest.testmod(question_4)

class Test(unittest.TestCase):

    def test_dot_product(self):
        x = question_4.Vector({"a": 1, "b": 3})
        y = question_4.Vector({"a": 2, "c": 1})

        xy_dot = x.dot_product(y)
        self.assertGreater(xy_dot, 0)

    def test_norm(self):
        x = question_4.Vector({"a": 1, "b": 3})

        x_norm = x.norm()
        self.assertGreater(x_norm, 0)

    def test_cosine(self):
        x = question_4.Vector({"a": 1, "b": 3})
        y = question_4.Vector({"a": 2, "c": 1})

        xy_dot = x.cosine(y)
        self.assertGreater(xy_dot, 0)

    def test_vsm(self):
        ds = Document.from_texts([documents.DOCUMENT_1, documents.DOCUMENT_2, documents.DOCUMENT_3])
        vsm = VSM(ds)

        query = "nobel physics britian idea"
        show(query)

        results = vsm.query(query)
        show(results)


if __name__ == "__main__":
    unittest.main()