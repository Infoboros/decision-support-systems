def normalize_matrix(matrix: [[float]]):
    summary = list(map(
        sum,
        zip(*matrix)
    ))
    return [
        [
            item / summary[index]
            for index, item in enumerate(row)
        ]
        for row in matrix
    ]


def print_matrix(matrix: [[float]]):
    print(
        '\n'.join(
            [
                ' '.join([str(round(el, 2)) for el in row])
                for row in matrix
            ]
        )
    )
    print()
