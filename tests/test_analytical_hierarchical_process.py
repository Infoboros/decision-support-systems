import pytest

from algorithm.analytical_hierarchical_process import MatrixProcessor, AnalyticalHierarchicalProcessor


@pytest.fixture()
def hierarchia():
    return [
        {
            'nodes': ['1'],
            'matrs': [
                [
                    [1,       1,       1,       4, 1,       1. / 2.],
                    [1,       1,       2,       4, 1,       1. / 2.],
                    [1,       1. / 2., 1,       5, 3,       1. / 2.],
                    [1. / 4., 1. / 4., 1. / 5., 1, 1. / 3., 1. / 3.],
                    [1,       1,       1. / 3., 3, 1,       1],
                    [2,       2,       2,       3, 1,       1],
                ]
            ]
        },
        {
            'nodes': ['2', '3', '4', '5', '6', '7'],
            'matrs': [
                [
                    [1, 1. / 3., 1. / 2.],
                    [3, 1, 3],
                    [2, 1. / 3., 1]
                ],
                [
                    [1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]
                ],

                [
                    [1, 5, 1],
                    [1. / 5., 1, 1. / 5.],
                    [1, 5, 1],
                ],
                [
                    [1, 9, 7],
                    [1. / 9., 1, 1. / 5.],
                    [1. / 7., 5, 1],
                ],

                [
                    [1, 1. / 2., 1],
                    [2, 1, 2],
                    [1, 1. / 2., 1]
                ],
                [
                    [1, 6, 4],
                    [1. / 6., 1, 1. / 3.],
                    [1. / 4., 3, 1]
                ],
            ]
        },
    ]


@pytest.fixture
def matr():
    # return [
    #     [1, 1, 1],
    #     [1, 1, 1],
    #     [1, 1, 1],
    # ]
    return [
        [1, 1. / 3., 1. / 2.],
        [3, 1, 3],
        [2, 1. / 3., 1]
    ]


def test_matrix(matr):
    processor = MatrixProcessor(matr)
    eigenvalues, lmax = processor.get_eigenvalues_and_lmax()
    IS = processor.get_is(lmax)
    OS = processor.get_os(IS)

    print()
    print(eigenvalues)
    print(IS)
    print(OS)

def test_hierarchical_processor(hierarchia):
    AnalyticalHierarchicalProcessor(hierarchia).calculate()
