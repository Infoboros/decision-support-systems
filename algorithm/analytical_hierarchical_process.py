import operator
from functools import reduce

from algorithm.utils import print_matrix


class MatrixProcessor:
    def __init__(self, matrix: [[float]]):
        self.matrix = matrix

    @property
    def n(self) -> int:
        return len(self.matrix)

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
            lambda geometry: geometry / sum_avg_geometry,
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


class AnalyticalHierarchicalProcessor:
    def __init__(self, hierarchical: list):
        self.hierarchical = hierarchical

    def calculate(self):
        vs = []
        for level in self.hierarchical:
            level_vs = []
            for matrix in level['matrs']:
                print_matrix(matrix)

                processor = MatrixProcessor(matrix)

                eigenvalues, lmax = processor.get_eigenvalues_and_lmax()
                IS = processor.get_is(lmax)
                OS = processor.get_os(IS)

                print()
                print('Собственные числа ', eigenvalues)
                print('Lmax ', lmax)
                print('Индекс согласованности ', IS)
                print('Отношение согласованности ', OS)

                level_vs.append(eigenvalues)

            vs.append(level_vs)

        Zs = [
            [1]
        ]
        for level_vs in vs:
            prevZs = Zs[-1]
            Zs.append(
                [
                    sum([
                        level_vs[indexZ][next_z_index] * z
                        for indexZ, z in enumerate(prevZs)
                    ])
                    for next_z_index in range(len(level_vs[0]))
                ]
            )

        print()
        offset = 1
        for level_z in Zs:
            print(' '.join([f'Z{index + offset}={z}' for index, z in enumerate(level_z)]))
            offset += len(level_z)

        return Zs
