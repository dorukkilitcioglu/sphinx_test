import numpy as np

from gha_aut_test.functions import relu
from tests.test_base import BaseTest


class FunctionsTest(BaseTest):
    def test_relu_non_negative(self):
        self.assertTrue((relu(np.array([-1, -2, 0.])) >= 0).all())

    def test_relu_no_change_positive(self):
        a = np.array([1., 2., 3.])
        self.assertTrue(np.array_equal(a, relu(a)))
