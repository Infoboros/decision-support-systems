

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