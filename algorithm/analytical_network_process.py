from algorithm.matrix import Matrix
from algorithm.utils import print_matrix


class AnalyticalNetworkProcessor:
    def __init__(self, macro_mps: list, micro_mps: list):
        self.macro_mps = macro_mps
        self.micro_mps = micro_mps

    @property
    def count_clusters(self):
        return len(
            set(
                map(
                    lambda cluster_info: cluster_info["cluster"],
                    self.macro_mps
                )
            )
        )

    def get_macro_weights(self) -> [[list]]:
        cluster_count = self.count_clusters
        macro_weights = Matrix.init_zero(cluster_count, cluster_count)

        for cluster_info in self.macro_mps:
            matrix = cluster_info["matr"]
            cluster = cluster_info["cluster"]
            directs = cluster_info["directs"]

            print(f"Для кластера {cluster}")
            print_matrix(matrix)

            processor = Matrix(matrix)
            eigenvalues = processor.get_eigenvalues()
            print("Собственные числа")
            print(eigenvalues)

            macro_weights.replace_part_column(cluster, directs, eigenvalues)

        return macro_weights.matrix

    def get_micro_synthesis(self) -> [[float]]:
        super_matrix = []
        for source in self.micro_mps:
            source_cluster = source["cluster"]
            print(f"Матрицы парных сравнений влияния кластера {source_cluster}")
            print()
            for element in source["elements"]:
                column = []
                print(f"Для элемента {element['element']}")
                for index, direct_mps in enumerate(element["directs"]):
                    print(f"На кластер {index}")
                    print_matrix(direct_mps)

                    processor = Matrix(direct_mps)
                    eigenvalues = processor.get_eigenvalues()
                    print(f"Собственные числа {eigenvalues}")
                    column += eigenvalues
                super_matrix.append(column)

        return list(zip(*super_matrix))

    def get_weighted_super_matrix(self, weights, super_matrix):
        elements_in_matrix = len(super_matrix) // self.count_clusters

        def get_weights_index(index):
            return index // elements_in_matrix

        return [
            [
                element * weights[get_weights_index(row_index)][get_weights_index(column_index)]
                for column_index, element in enumerate(row)
            ]
            for row_index, row in enumerate(super_matrix)
        ]

    def get_limit(self, basis, k):
        current = Matrix.mult_matrix(basis, basis)
        for _ in range(k - 2):
            current = Matrix.mult_matrix(current, basis)

        return current

    def get_normalized(self, limit_matrix, elements) -> [float]:
        results = list(zip(*limit_matrix))[0]
        names = elements["names"]
        counts = elements["counts"]

        print("Абсолютные приоритеты:")
        print_matrix(zip(names, results))

        print("Суммы")
        start = 0
        ranged = []
        for count in counts:
            ranged.append(results[start: start+count])
            start += count
        sums = [sum(cluster) for cluster in ranged]
        print(sums)

        normalized = [
            element / sums[sum_index]
            for sum_index, cluster in enumerate(ranged)
            for element in cluster
        ]
        print("Нормализованные абсолютные приоритеты")
        print_matrix(zip(names, normalized))



    def calculate(self, elements):
        macro_weights = self.get_macro_weights()

        print("Матрица показывающая степень влияния кластеров друг на друга")
        print_matrix(macro_weights)

        micro_synthesis = self.get_micro_synthesis()
        print("Невзвешенная суперматрица")
        print_matrix(micro_synthesis)

        weights_synthesis = self.get_weighted_super_matrix(macro_weights, micro_synthesis)
        print("Взвешенная суперматрица")
        print_matrix(weights_synthesis)

        k = len(weights_synthesis) * len(weights_synthesis)
        limit_matrix = self.get_limit(weights_synthesis, k)
        print(f"Предельная матрица при k={k}")
        print_matrix(limit_matrix)

        return self.get_normalized(limit_matrix, elements)
