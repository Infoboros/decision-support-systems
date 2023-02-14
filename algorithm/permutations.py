import itertools
from math import log

from algorithm.step_logger import StepLogger
from algorithm.utils import normalize_matrix


class Permutations:
    def __init__(self, alternatives: [[float]], weights: [float], criteria_sign, p=5):
        self.alternatives = alternatives

        self.logger = StepLogger()
        self.logger.write(
            'Альтернативы',
            alternatives
        )

        self.logger.write(
            'Важность криетриев (Ненормированная)',
            weights
        )
        self.weights = self.__normalize_weights(weights)
        self.logger.write(
            'Важность криетриев (Нормированная)',
            self.weights
        )

        self.criteria_sign = criteria_sign
        self.p = p

    @staticmethod
    def __normalize_weights(weights: [float]) -> [float]:
        summary = sum(weights)
        return list(
            map(
                lambda weight: weight / summary,
                weights
            )
        )

    def __get_normalized_alternatives(self) -> [[float]]:
        normalized_alternatives = normalize_matrix(self.alternatives)
        self.logger.write(
            'Б) Нормированная матрица принятия решений (p):',
            normalized_alternatives
        )
        return normalized_alternatives

    def __get_entropy(self, normalized_alternatives: [[float]]) -> [float]:
        k = 1 / log(len(normalized_alternatives))
        entropy = [
            -k * sum([
                Pij * log(Pij)
                for Pij in row
            ])
            for row in zip(*normalized_alternatives)
        ]
        self.logger.write(
            'В) Энтропия (Е):',
            entropy
        )

        return entropy

    def __get_invert_entropy(self, entropy: [float]) -> [float]:
        invert_entropy = [
            1 - e
            for e in entropy
        ]
        self.logger.write(
            'Г) Инвертированная энтропия (l):',
            invert_entropy
        )

        return invert_entropy

    def __get_complex_weights(self, invert_entropy: [float]) -> [float]:
        summary = sum([
            ie * self.weights[index]
            for index, ie in enumerate(invert_entropy)
        ])

        complex_weights = [
            ie / summary * self.weights[index]
            for index, ie in enumerate(invert_entropy)
        ]

        self.logger.write(
            'Д) Комплексная важность (λ_j^k):',
            complex_weights
        )

        return complex_weights

    def get_complex_weights(self):
        self.logger.write(
            'Матрица принятия решений',
            self.alternatives
        )

        normalized_alternatives = self.__get_normalized_alternatives()

        entropy = self.__get_entropy(normalized_alternatives)
        invert_entropy = self.__get_invert_entropy(entropy)

        return self.__get_complex_weights(invert_entropy)

    def get_all_permutations(self) -> [[int]]:
        permutations = list(
            itertools.permutations([
                index
                for index in range(len(self.alternatives))
            ])
        )
        self.logger.write(
            'Все возможные перестановки',
            permutations
        )
        return permutations

    def __get_C_H(self, permutation: [int]) -> [[int]]:
        CsP = []
        HsP = []
        for wrapper_index in range(len(permutation) - 1):
            for index in range(wrapper_index + 1, len(permutation)):
                left = self.alternatives[permutation[wrapper_index]]
                right = self.alternatives[permutation[index]]

                Cs = []
                Hs = []
                for criteria, (criteria_left, criteria_right) in enumerate(zip(left, right)):
                    sign = self.criteria_sign[criteria]
                    if criteria_left * sign > criteria_right * sign:
                        Cs.append(criteria)
                    if criteria_left * sign < criteria_right * sign:
                        Hs.append(criteria)

                CsP.append(Cs)
                HsP.append(Hs)

        self.logger.write(
            'Перестановка',
            permutation
        )

        self.logger.write(
            'С',
            CsP
        )
        self.logger.write(
            'H',
            HsP
        )

        return {
            'CsP': CsP,
            'HsP': HsP,
        }

    def get_C_H(self, permutations: [[int]]) -> [dict]:
        return {
            permutation: self.__get_C_H(permutation)
            for permutation in permutations
        }

    def __sum_L(self, criteriaes, complex_weights) -> float:
        return sum([
            complex_weights[criteria]
            for criteria in criteriaes
        ])

    def _get_B(self, C, H, complex_weights):
        return sum([
            self.__sum_L(c, complex_weights)
            for c in C
        ]) \
            - \
            sum([
                self.__sum_L(h, complex_weights)
                for h in H
            ])

    def get_Bs(self, C_H: dict, complex_weights):
        Bs = [
            [permutation, self._get_B(c_h['CsP'], c_h['HsP'], complex_weights)]
            for permutation, c_h in C_H.items()
        ]

        self.logger.write(
            'Bs',
            Bs
        )

        return Bs

    def execute(self):
        complex_weights = self.get_complex_weights()
        permutations = self.get_all_permutations()

        C_H = self.get_C_H(permutations)
        Bs = self.get_Bs(C_H, complex_weights)

        sorted_Bs = list(sorted(Bs, key=lambda x: -x[1]))
        self.logger.write(
            'Отсортированные B',
            sorted_Bs
        )
