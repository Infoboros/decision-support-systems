from copy import copy
from math import log

from algorithm.step_logger import StepLogger
from algorithm.utils import normalize_matrix


class DisplacedIdeal:
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

    def get_decision_making_matrix(self) -> [[float]]:
        self.logger.write(
            'Матрица принятия решений(x)',
            self.alternatives
        )
        return self.alternatives

    def __transpose_and_map_alternatives(self, funcs) -> list:
        return [
            funcs[index](column)
            for index, column in enumerate(zip(*self.alternatives))
        ]

    def get_major(self) -> [float]:
        major = self.__transpose_and_map_alternatives([
            max if sign > 0 else min
            for sign in self.criteria_sign
        ])
        self.logger.write(
            '1а.Идеальный объект',
            major
        )
        return major

    def get_minor(self) -> [float]:
        minor = self.__transpose_and_map_alternatives([
            min if sign > 0 else max
            for sign in self.criteria_sign
        ])
        self.logger.write(
            '1б.Неидеальный объект',
            minor
        )
        return minor

    @staticmethod
    def __get_relative_alternative(alternative: [float], minor: [float], major: [float]) -> [float]:
        return [
            (major[i] - criteria) / (major[i] - minor[i])
            for i, criteria in enumerate(alternative)
        ]

    def get_relative_alternatives(self, minor: [float], major: [float]) -> [[float]]:
        relative_alternatives = [
            self.__get_relative_alternative(alternative, minor, major)
            for alternative in self.alternatives
        ]
        self.logger.write(
            '2.Переход к относительным единицам (d)',
            relative_alternatives
        )
        return relative_alternatives

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
            '3.Определение комплексной важности\n'
            'А) Матрица принятия решений',
            self.alternatives
        )

        normalized_alternatives = self.__get_normalized_alternatives()

        entropy = self.__get_entropy(normalized_alternatives)
        invert_entropy = self.__get_invert_entropy(entropy)

        return self.__get_complex_weights(invert_entropy)

    @staticmethod
    def __get_p(alternatives: [[float]], weights: [float], p: int) -> [float]:
        return [
            pow(
                sum([
                    pow(
                        weights[j] * (1 - criteria),
                        p
                    )
                    for j, criteria in enumerate(alternative)
                ]),
                1. / p
            )
            for alternative in alternatives
        ]

    def get_p(self, alternative: [[float]], weights: [float]) -> []:
        p = [
            list(row)
            for row in zip(
                *[
                    self.__get_p(alternative, weights, p + 1)
                    for p in range(self.p)
                ]
            )
        ]

        self.logger.write(
            '4.	Определение расстояния от неидеального объекта до i-го:',
            p
        )

        return p

    def __sorting_alternative(self, p: [float]):
        sorted_indexes = []

        copy_p = [
            (index, criteria)
            for index, criteria in enumerate(p)
        ]
        while copy_p:

            maximum = copy_p[0][1]
            maximum_index = 0

            for index, (base_index, criteria) in enumerate(copy_p):
                if criteria > maximum:
                    maximum_index = index
                    maximum = criteria

            sorted_indexes.append(copy_p[maximum_index][0])
            copy_p.pop(maximum_index)

        return sorted_indexes

    def sorting_indexes(self, ps: [float]):
        sorting_indexes = [
            self.__sorting_alternative(p)
            for p in zip(*ps)
        ]

        self.logger.write(
            '5.	Ранжирование альтернатив и отсеивание:',
            [
                '>'.join([f'S{index + 1}' for index in sorted_indexes]) + '\n'
                for sorted_indexes in sorting_indexes
            ]
        )
        return sorting_indexes

    def selection(self, sorting_indexes: [[float]]) -> int:
        count_bad = [0 for _ in sorting_indexes[0]]
        for sorting_index in sorting_indexes:
            count_bad[sorting_index[-1]] += 1

        self.logger.write(
            'Количество раз, когда вариант является худшим',
            count_bad
        )

        maximum_index = 0
        for index, count in enumerate(count_bad):
            if count_bad[maximum_index] < count:
                maximum_index = index
        self.logger.write(
            'Худший и отброшенный элемент',
            [f'S{maximum_index + 1}']
        )

        return maximum_index

    def execute(self):
        self.get_decision_making_matrix()

        major = self.get_major()
        minor = self.get_minor()

        ds = self.get_relative_alternatives(minor, major)
        complex_weights = self.get_complex_weights()

        ps = self.get_p(ds, complex_weights)
        sorting_indexes = self.sorting_indexes(ps)

        selected_index = self.selection(sorting_indexes)

        copy_alternatives = copy(self.alternatives)
        copy_alternatives.pop(selected_index)

        return DisplacedIdeal(
            copy_alternatives,
            self.weights,
            self.criteria_sign,
            self.p
        )
