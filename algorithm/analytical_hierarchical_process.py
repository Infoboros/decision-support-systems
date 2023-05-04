from algorithm.matrix import Matrix
from algorithm.utils import print_matrix


class AnalyticalHierarchicalProcessor:
    def __init__(self, hierarchical: list):
        self.hierarchical = hierarchical

    def calculate(self):
        vs = []
        for level in self.hierarchical:
            level_vs = []
            for matrix in level['matrs']:
                print_matrix(matrix)

                processor = Matrix(matrix)

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
