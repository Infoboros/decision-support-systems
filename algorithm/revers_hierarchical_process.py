from algorithm.analytical_hierarchical_process import MatrixProcessor
from algorithm.utils import print_matrix, normalize_matrix


class ReversHierarchicalProcessor:

    def __init__(self, Za: list, hierarchical: list):
        print('Оценки, выраженные в собственных числах:')
        print_matrix(Za)

        self.Za = normalize_matrix(Za)
        print('Нормированные оценки:')
        print_matrix(self.Za)

        self.hierarchical = hierarchical

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

    def get_Zs(self) -> []:
        Zs = [self.Za]
        for level in self.hierarchical:
            Z = Zs[-1]

            V = list(
                zip(
                    *list(
                        map(
                            lambda E: MatrixProcessor(E).get_eigenvalues(),
                            level
                        )
                    )
                )
            )
            print('C.В.')
            print_matrix(V)
            Zs.append(self.mult_matrix(Z, V))
        return Zs
