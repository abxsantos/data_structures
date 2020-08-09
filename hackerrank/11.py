def spiral_matrix(n):
    """
    Given a number n generate a NxN spiral matrix
    """
    spiral = []
    return spiral


class TestSpiralMatrix(object):
    def test_spiral_matrix(self):
        expected_matrix = [
            [1,   2,  3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10,  9,  8, 7]
        ]
        assert spiral_matrix(4) == expected_matrix
