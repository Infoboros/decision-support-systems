import operator
from functools import reduce


class Matrix:
    def __init__(self, matrix: [[float]]):
        self.matrix = matrix

    @property
    def n(self) -> int:
        return len(self.matrix)

    @staticmethod
    def init_zero(n: int, m: int):
        return Matrix(
            [
                [
                    0.0
                    for _ in range(n)
                ]
                for _ in range(m)
            ]
        )

    @staticmethod
    def mult_matrix(a, b):
        transposed_b = list(zip(*b))
        return [[
            sum(
                ele_a * ele_b
                for ele_a, ele_b in zip(row_a, col_b)
            )
            for col_b in transposed_b
        ] for row_a in a
        ]

    def replace_part_column(self, column: int, positions: list, sources: list):
        for position, source in zip(positions, sources):
            self.matrix[position][column] = source

    def get_eigenvalues_and_lmax(self) -> ([float], float):
        norm_eigenvalues = self.get_eigenvalues()

        sum_column = list(map(sum, zip(*self.matrix)))

        lmax = sum([
            norm_eigenvalues[index] * b
            for index, b in enumerate(sum_column)
        ])

        return norm_eigenvalues, lmax

    def get_eigenvalues(self):
        n = self.n
        avg_geometry = [
            pow(reduce(operator.mul, row, 1), 1. / n)
            for row in self.matrix
        ]
        sum_avg_geometry = sum(avg_geometry)
        norm_eigenvalues = list(map(
            lambda geometry: geometry / sum_avg_geometry if sum_avg_geometry else 0.0,
            avg_geometry
        ))
        return norm_eigenvalues

    def get_is(self, lmax: float) -> float:
        return (lmax - self.n) / (self.n - 1)

    def get_os(self, IS: float) -> float:
        return IS / {
            1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.9,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49,
            11: 1.51,
            12: 1.54,
            13: 1.56,
            14: 1.57,
            15: 1.59
        }[self.n]
