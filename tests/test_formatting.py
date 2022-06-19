import numpy as np
import unittest
import pandas as pd

from cerberus.helper.formatting import *

data = pd.read_csv('./exampleData/CaliforniaHousing.csv')


to_pred = data.tail(10)

X = np.array([[ 1.10000000e+01,  5.93258427e+00,  1.13483146e+00,
                1.25700000e+03,  2.82471910e+00,  3.92900000e+01,
               -1.21320000e+02,  3.56730000e+00],
              [ 1.50000000e+01,  6.14583333e+00,  1.14120370e+00,
                1.20000000e+03,  2.77777778e+00,  3.93300000e+01,
               -1.21400000e+02,  3.51790000e+00]])

X = pred_input(to_pred, 2, 'target', 5)[0]
y = pred_input(to_pred, 2, 'target', 5)[1]


class TestFormatting(unittest.TestCase):


    def test_pred_input(self):
        np.testing.assert_allclose(pred_input(to_pred, 2, 'target', 5)[0], X)



if __name__ == '__main__':
    unittest.main()
