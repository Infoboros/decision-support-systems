from algorithm.step_logger import StepLogger


class DisplacedIdeal:
    def __init__(self, alternatives: [[float]], weights: [float]):
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
            'Матрица принятия решений',
            self.alternatives
        )
        return self.alternatives