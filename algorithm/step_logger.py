class Step:
    def __init__(self, name: str, data):
        self.name = name
        self.data = data

    @staticmethod
    def __format_row(row: list) -> str:
        return ' '.join(map(str, row)) + '\n'

    @staticmethod
    def __format_data(data):
        if type(data[0]) is list:
            formatted_list = map(
                lambda row: Step.__format_row(row),
                data
            )
        else:
            formatted_list = Step.__format_row(data)

        return ''.join(formatted_list)

    def __str__(self):
        return f'\n' \
               f'{self.name}\n' \
               f'{self.__format_data(self.data)}'


class StepLogger:
    def __init__(self):
        self.log = []

    def write(self, name_step: str, data):
        self.log.append(
            Step(
                name_step,
                data
            )
        )

    def get_step(self, index: int) -> Step:
        return self.log[index]

    def __str__(self):
        return '\n'.join([
            str(step)
            for step in self.log
        ])
